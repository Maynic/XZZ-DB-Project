import React, { useState, useEffect, useRef } from 'react';
import axios from "axios";

import { API_URL } from "constants";

import {
    Modal,
    ModalOverlay,
    ModalContent,
    ModalHeader,
    ModalFooter,
    ModalBody,
    ModalCloseButton,
    Button,
    Input,
    FormControl,
    FormLabel,
    useDisclosure,
    useColorModeValue,
    Icon,
    useStyleConfig,
    Select,
} from '@chakra-ui/react'

import {
    MdOutlineAdd,
} from "react-icons/md";


export default function VisitorDetail(props) {
    const [visitorData, setVisitorData] = useState({
        pk: 0,
        visitor_name: '',
        email: '',
        birth_date: '',
        phone: '',
        address: '',
        city: '',
        state: '',
        zip: '',
        visitor_type: '',
    });
    const API_Visitor = useRef(API_URL + "visitor/");

    useEffect(() => {
        if (props.visitor) {
            const { pk, visitor_name, email, birth_date, phone, address, city, state, zip, visitor_type } = props.visitor;
            setVisitorData({ pk, visitor_name, email, birth_date, phone, address, city, state, zip, visitor_type });
        }
    }, []);

    const onChange = (e) => {
        setVisitorData({ ...visitorData, [e.target.name]: e.target.value });
    };

    const createVisitor = (e) => {
        e.preventDefault();
        axios.post(API_Visitor.current, visitorData).then(() => {
            props.resetState();
            props.toggle();
        });
    };

    const editVisitor = (e) => {
        e.preventDefault();
        axios.put(API_Visitor.current + visitorData.pk, visitorData).then(() => {
            props.resetState();
            props.toggle();
        });
    };

    const defaultIfEmpty = (value) => {
        return value === '' ? '' : value;
    };

    const { ...rest } = props;
    const { isOpen, onOpen, onClose } = useDisclosure()
    const initialRef = React.useRef(null)
    const finalRef = React.useRef(null)

    // Styling
    const bgButton = useColorModeValue("secondaryGray.300", "whiteAlpha.100");
    const bgHover = useColorModeValue(
        { bg: "secondaryGray.400" },
        { bg: "whiteAlpha.50" }
    );
    const bgFocus = useColorModeValue(
        { bg: "secondaryGray.300" },
        { bg: "whiteAlpha.100" }
    );
    const iconColor = useColorModeValue("brand.500", "white");



    return (
        <>
            <Button onClick={() => { onOpen() }}
                align='center'
                justifyContent='center'
                bg={bgButton}
                _hover={bgHover}
                _focus={bgFocus}
                _active={bgFocus}
                w='37px'
                h='37px'
                lineHeight='100%'
                borderRadius='10px'
                {...rest}>
                <Icon as={MdOutlineAdd} color={iconColor} w='24px' h='24px' />

            </Button>

            <Modal
                initialFocusRef={initialRef}
                finalFocusRef={finalRef}
                isOpen={isOpen}
                onClose={onClose}
                closeOnOverlayClick={false}
                scrollBehavior={'inside'}
            // scrollBehavior={'outside'}
            >
                <ModalOverlay
                    bg='blackAlpha.300'
                    backdropFilter='blur(3px)'
                />

                <ModalContent>
                    {/* <ModalHeader align='center'>Add/Modify Visitor</ModalHeader> */}
                    <ModalHeader >Add/Modify Visitor</ModalHeader>
                    {/* <ModalCloseButton /> */}
                    <ModalBody pb={6}>

                        <FormControl>
                            <FormLabel>Name</FormLabel>
                            <Input
                                name='visitor_name'
                                type='text'
                                placeholder='Name'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(visitorData.visitor_name)}
                            />
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Email</FormLabel>
                            <Input
                                name='email'
                                type='email'
                                placeholder='Email'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(visitorData.email)}
                            />
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Birthday</FormLabel>
                            <Input
                                name='birth_date'
                                type='date'
                                placeholder='Birthday'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(visitorData.birth_date)}
                            />
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Phone</FormLabel>
                            <Input
                                name='phone'
                                type='number'
                                placeholder='Phone'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(visitorData.phone)}
                            />
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Street</FormLabel>
                            <Input
                                name='address'
                                type='text'
                                placeholder='Street'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(visitorData.address)}
                            />
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>City</FormLabel>
                            <Input
                                name='city'
                                type='text'
                                placeholder='City'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(visitorData.city)}
                            />
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>State</FormLabel>
                            <Input
                                name='state'
                                type='text'
                                placeholder='State'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(visitorData.state)}
                            />
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>ZIP Code</FormLabel>
                            <Input
                                name='zip'
                                type='number'
                                placeholder='ZIP Code'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(visitorData.zip)}
                            />
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Visitor Type</FormLabel>
                            <Select
                                name='visitor_type'
                                type='text'
                                placeholder='Visitor Type'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(visitorData.visitor_type)}>
                                <option value='IN'>Individual</option>
                                <option value='GR'>Group</option>
                                <option value='ME'>Member</option>
                                <option value='ST'>Student</option>
                            </Select>
                        </FormControl>

                    </ModalBody>

                    <ModalFooter>
                        <Button colorScheme='blue' mr={3} onClick={props.visitor ? editVisitor : createVisitor}>
                            Save
                        </Button>
                        <Button onClick={onClose} ref={initialRef}>Cancel</Button>
                    </ModalFooter>
                </ModalContent>
            </Modal>
        </>
    )
}

