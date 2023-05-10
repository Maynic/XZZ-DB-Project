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
        payment_method: 'CA',
        payment_amount: '',
        name_on_card: '',
        card_number: '',
        expiration_date: 0,
        cvv: 0,
        order: '',
    });


    const [Error, setError] = useState(
        {
            hasError: false,
            errorInfo: ''
        }
    )

    const API_Full = useRef(API_URL + "payment/");
    const { resetState, isEdit, row, } = props;
    const { isOpen, onOpen, onClose } = useDisclosure()
    const initialRef = React.useRef(null)
    const finalRef = React.useRef(null)

    useEffect(() => {
        if (row?.values) {
            var ed = ''
            const { payment_method, payment_amount, name_on_card, card_number, id, expiration_date, cvv, order } = row?.original;
            if(expiration_date){
                ed = expiration_date.slice(0, 10)
            }
            setData({ pk: id, payment_method, payment_amount, name_on_card, card_number, expiration_date:ed,cvv, order });
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
                                <div>Modify Payment</div>
                                <AlertDelete deleteData={deleteData} />
                            </>
                            ) : (<><div>Add Payment</div></>)}
                        </Flex>
                    </ModalHeader>

                    <ModalBody pb={6}>

                        <FormControl mt={4}>
                            <FormLabel>Method</FormLabel>
                            <Select
                                name='payment_method'
                                type='text'
                                // placeholder='Cash'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.payment_method)}>
                                <option value='CA'>Cash</option>
                                <option value='CR'>Credit</option>
                                <option value='DE'>Debit</option>
                            </Select>
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Amount</FormLabel>
                            <Input
                                name='payment_amount'
                                type='number'
                                placeholder='0 - 999999'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.payment_amount)}
                            />
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Name On Card</FormLabel>
                            <Input
                                name='name_on_card'
                                type='text'
                                placeholder='Full Name'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.name_on_card)}>
                            </Input>
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Card Number</FormLabel>
                            <Input
                                name='card_number'
                                type='text'
                                placeholder='0000000000000000'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.card_number)}>
                            </Input>
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Expiration Date</FormLabel>
                            <FormHelperText>Day will be ignored.</FormHelperText>
                            <Input
                                name='expiration_date'
                                type='date'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.expiration_date)}>
                            </Input>
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>CVV</FormLabel>
                            <Input
                                name='cvv'
                                type='text'
                                placeholder='000'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.cvv)}
                            />
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Order ID</FormLabel>
                            <Input
                                name='order'
                                type='number'
                                placeholder='0'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.order)}
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

