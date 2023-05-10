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
        show_name: '',
        show_description: '',
        show_type: '',
        start_time: '',
        end_time: 0,
        show_accessible: 0,
        show_price: '',
    });


    const [Error, setError] = useState(
        {
            hasError: false,
            errorInfo: ''
        }
    )

    const API_Full = useRef(API_URL + "show/");
    const { resetState, isEdit, row, } = props;
    const { isOpen, onOpen, onClose } = useDisclosure()
    const initialRef = React.useRef(null)
    const finalRef = React.useRef(null)

    useEffect(() => {
        if (row?.values) {
            const { show_name, show_description, show_type, start_time, id, end_time, show_accessible, show_price } = row?.original;
            const st = start_time.slice(0, 16)
            const et = end_time.slice(0, 16)
            setData({ pk: id, show_name, show_description, show_type, start_time: st, end_time: et, show_accessible, show_price });
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

                        <FormControl>
                            <FormLabel>Show Name</FormLabel>
                            <Input
                                name='show_name'
                                type='text'
                                placeholder='Show'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.show_name)}
                            />
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Description</FormLabel>
                            <Input
                                name='show_description'
                                type='text'
                                placeholder='Description'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.show_description)}
                            />
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Show Type</FormLabel>
                            <Select
                                name='show_type'
                                type='text'
                                // placeholder='Full Name'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.show_type)}>
                                <option value='Drama'>Drama</option>
                                <option value='Musical'>Musical</option>
                                <option value='Comedy'>Comedy</option>
                                <option value='Horror'>Horror</option>
                                <option value='Adventure'>Adventure</option>
                            </Select>
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Start Time</FormLabel>
                            <Input
                                name='start_time'
                                type='datetime-local'
                                // placeholder='0000000000000000'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.start_time)}>
                            </Input>
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>End Time</FormLabel>
                            {/* <FormHelperText>Day will be ignored.</FormHelperText> */}
                            <Input
                                name='end_time'
                                type='datetime-local'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.end_time)}>
                            </Input>
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Wheelchair Accessible</FormLabel>
                            <Select
                                name='show_accessible'
                                type='text'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.show_accessible)}>
                                <option value='Yes'>Yes</option>
                                <option value='No'>No</option>
                            </Select>
                        </FormControl>

                        <FormControl mt={4}>
                            <FormLabel>Price</FormLabel>
                            <Input
                                name='show_price'
                                type='number'
                                placeholder='0'
                                onChange={onChange}
                                defaultValue={defaultIfEmpty(data.show_price)}
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

