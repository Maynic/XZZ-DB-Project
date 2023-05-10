import React, { useState, useEffect, useRef } from 'react';
import axios from "axios";

import { API_URL } from "constants";

import {
    AlertDialog,
    AlertDialogBody,
    AlertDialogFooter,
    AlertDialogHeader,
    AlertDialogContent,
    AlertDialogOverlay,
    Modal,
    ModalOverlay,
    ModalContent,
    ModalHeader,
    ModalFooter,
    ModalBody,
    Button,
    Input,
    FormControl,
    FormLabel,
    useDisclosure,
    useColorModeValue,
    Icon,
    Select,
    Flex,
    Alert,
    AlertIcon,
    AlertTitle,
    AlertDescription,
} from '@chakra-ui/react'

import {
    MdOutlineAdd, MdOutlineEdit
} from "react-icons/md";

function AlertDelete(props) {
    const { isOpen, onOpen, onClose } = useDisclosure()
    const cancelRef = React.useRef()
    const { deleteData } = props

    return (
        <>
            <Button colorScheme='red'
                onClick={onOpen}
                align='center'
                justifyContent='center'>
                Delete
            </Button>

            <AlertDialog
                isOpen={isOpen}
                leastDestructiveRef={cancelRef}
                onClose={onClose}
                motionPreset='scale'
                isCentered
            >
                <AlertDialogOverlay>
                    <AlertDialogContent>
                        <AlertDialogHeader fontSize='lg' fontWeight='bold'>
                            Delete Data
                        </AlertDialogHeader>

                        <AlertDialogBody>
                            Are you sure? You can't undo this action afterwards.
                        </AlertDialogBody>

                        <AlertDialogFooter>
                            <Button ref={cancelRef} onClick={onClose}>
                                Cancel
                            </Button>
                            <Button colorScheme='red' onClick={deleteData} ml={3}>
                                Delete
                            </Button>
                        </AlertDialogFooter>
                    </AlertDialogContent>
                </AlertDialogOverlay>
            </AlertDialog>
        </>
    )
}

function AlertError(props) {
    const { message } = props
    return (
        <>
            <Alert status='error'>
                <AlertIcon />
                <AlertTitle>Failed!</AlertTitle>
                <AlertDescription>
                    Please check data format!
                </AlertDescription>

            </Alert>

        </>
    )
}

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
        visitor_type: 'IN',
    });


    const [Error, setError] = useState(
        {
            hasError: false,
            errorInfo: ''
        }
    )

    const API_Visitor = useRef(API_URL + "visitor/");
    const { resetState, isEdit, row, } = props;
    const { isOpen, onOpen, onClose } = useDisclosure()
    const initialRef = React.useRef(null)
    const finalRef = React.useRef(null)

    useEffect(() => {
        if (row?.values) {
            const { address, birth_date, city, email, id, phone, state, visitor_name, visitor_type, zip, } = row?.original;
            const bd = birth_date.slice(0, 10)
            setVisitorData({ pk: id, visitor_name, email, birth_date: bd, phone, address, city, state, zip, visitor_type });
        }
    }, []);


    const onChange = (e) => {
        setVisitorData({ ...visitorData, [e.target.name]: e.target.value });
    };

    const createVisitor = (e) => {
        e.preventDefault();
        axios.post(API_Visitor.current, visitorData).then(() => {
            resetState();
            setError({ hasError: false, errorInfo: '' });
            onClose();
        }).catch(error => {
            setError({ hasError: true, errorInfo: error.response.data });
            // console.log(error.response.data)
        });
    };

    const editVisitor = (e) => {
        e.preventDefault();
        axios.put(API_Visitor.current + visitorData.pk, visitorData).then(() => {
            resetState();
            setError({ hasError: false, errorInfo: '' });
            onClose();
        });
    };

    const deleteData = (e) => {
        e.preventDefault();
        axios.delete(API_Visitor.current + visitorData.pk).then(() => {
            resetState();
            onClose();
        });
    };

    const defaultIfEmpty = (value) => {
        return value === '' ? '' : value;
    };

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
            {isEdit ? (
                <Button onClick={() => {
                    onOpen();
                }}
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
                // {...rest}
                >
                    <Icon as={MdOutlineEdit} color={iconColor} w='24px' h='24px' />

                </Button>) : (
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
                // {...rest}
                >
                    <Icon as={MdOutlineAdd} color={iconColor} w='24px' h='24px' />

                </Button>
            )}

            < Modal
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
                    {Error.hasError ? (
                        <AlertError />
                    ) : (<></>)}

                    <ModalHeader >
                        <Flex justifyContent="space-between" alignItems="center" w="100%">

                            {isEdit ? (<>
                                <div>Modify Visitor</div>
                                <AlertDelete deleteData={deleteData} />
                            </>
                            ) : (<><div>Add Visitor</div></>)}
                        </Flex>
                    </ModalHeader>

                    <ModalBody pb={6}>

                        <FormControl>
                            <FormLabel>Name</FormLabel>
                            <Input
                                name='visitor_name'
                                type='text'
                                placeholder='Full Name'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(visitorData.visitor_name)}
                            />
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Email</FormLabel>
                            <Input
                                name='email'
                                type='email'
                                placeholder='addr@example.com'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(visitorData.email)}
                            />
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Birthday</FormLabel>
                            <Input
                                name='birth_date'
                                type='date'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(visitorData.birth_date)}
                            />
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Phone</FormLabel>
                            <Input
                                name='phone'
                                type='number'
                                placeholder='0123456789'
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
                                placeholder='NY'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(visitorData.state)}
                            />
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>ZIP Code</FormLabel>
                            <Input
                                name='zip'
                                type='number'
                                placeholder='12345'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(visitorData.zip)}
                            />
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Visitor Type</FormLabel>
                            <Select
                                name='visitor_type'
                                type='text'
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
                        {isEdit ? (
                            <Button colorScheme='blue' mr={3} onClick={editVisitor}>
                                Save Change
                            </Button>) : (
                            <Button colorScheme='blue' mr={3} onClick={createVisitor}>
                                Add
                            </Button>
                        )}
                        <Button onClick={function () { onClose(); setError({ hasError: false, errorInfo: '' }) }} ref={initialRef}>Cancel</Button>
                    </ModalFooter>
                </ModalContent>
            </Modal >
        </>
    )
}

