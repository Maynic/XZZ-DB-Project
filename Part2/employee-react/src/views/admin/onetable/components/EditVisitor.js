import React, { useState, useEffect, useRef } from 'react';
import axios from "axios";
import VisitorDetail from "views/admin/onetable/components/VisitorDetail";

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
    MdOutlineEdit,
} from "react-icons/md";


export default function EditVisitor(props) {
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
                <Icon as={MdOutlineEdit} color={iconColor} w='24px' h='24px' />

            </Button>
            <VisitorDetail
                // resetState={this.props.resetState}
                // toggle={this.toggle}
                // student={this.props.student}
            />

        </>
    )
}

