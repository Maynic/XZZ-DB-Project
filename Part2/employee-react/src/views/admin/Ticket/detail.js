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
    FormHelperText,
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

function AlertError() {
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

export default function Detail(props) {
    const [data, setData] = useState({
        pk: 0,
        order: '',
        visitor: '',
        visit_date: '',
        ticket_method: 0,
        ticket_price: '',
    });


    const [Error, setError] = useState(
        {
            hasError: false,
            errorInfo: ''
        }
    )

    const API_Full = useRef(API_URL + "ticket/");
    const { resetState, isEdit, row, } = props;
    const { isOpen, onOpen, onClose } = useDisclosure()
    const initialRef = React.useRef(null)
    const finalRef = React.useRef(null)

    useEffect(() => {
        if (row?.values) {
            const { order, visitor, visit_date, id, ticket_method, ticket_price } = row?.original;
            const st = visit_date.slice(0, 10)
            setData({ pk: id, order, visitor, visit_date: st, ticket_method, ticket_price });
        }
    }, []);


    const onChange = (e) => {
        setData({ ...data, [e.target.name]: e.target.value });
    };

    const createVisitor = (e) => {
        e.preventDefault();
        axios.post(API_Full.current, data).then(() => {
            resetState();
            setError({ hasError: false, errorInfo: '' });
            onClose();
        }).catch(error => {
            setError({ hasError: true, errorInfo: error.response.data });
        });
    };

    const editVisitor = (e) => {
        e.preventDefault();
        axios.put(API_Full.current + data.pk, data).then(() => {
            resetState();
            setError({ hasError: false, errorInfo: '' });
            onClose();
        }).catch(error => {
            setError({ hasError: true, errorInfo: error.response.data });
        });
    };

    const deleteData = (e) => {
        e.preventDefault();
        axios.delete(API_Full.current + data.pk).then(() => {
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
                                <div>Modify Show</div>
                                <AlertDelete deleteData={deleteData} />
                            </>
                            ) : (<><div>Add Show</div></>)}
                        </Flex>
                    </ModalHeader>

                    <ModalBody pb={6}>

                        <FormControl mt={4}>
                            <FormLabel>Method</FormLabel>
                            <Select
                                name='ticket_method'
                                type='text'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.ticket_method)}>
                                <option value='Online'>Online</option>
                                <option value='Onsite'>Onsite</option>
                            </Select>
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Visit Date</FormLabel>
                            <Input
                                name='visit_date'
                                type='date'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.visit_date)}>
                            </Input>
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Price</FormLabel>
                            <Input
                                name='ticket_price'
                                type='number'
                                placeholder='0'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.ticket_price)}
                            />
                        </FormControl>

                        <FormControl>
                            <FormLabel>Order ID</FormLabel>
                            <Input
                                name='order'
                                type='number'
                                placeholder='0'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.order)}
                            />
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Visitor ID</FormLabel>
                            <Input
                                name='visitor'
                                type='number'
                                placeholder='0'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.visitor)}
                            />
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

