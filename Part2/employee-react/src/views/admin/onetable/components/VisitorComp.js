import React, { useState, useEffect } from 'react';
import { Button, Form, FormGroup, Input, Label } from 'reactstrap';
import axios from 'axios';
import { API_URL } from '../constants';

const NewStudentForm = (props) => {
    const [studentData, setStudentData] = useState({
        pk: 0,
        name: '',
        email: '',
        document: '',
        phone: '',
    });

    useEffect(() => {
        if (props.student) {
            const { pk, name, document, email, phone } = props.student;
            setStudentData({ pk, name, document, email, phone });
        }
    }, [props.student]);

    const onChange = (e) => {
        setStudentData({ ...studentData, [e.target.name]: e.target.value });
    };

    const createStudent = (e) => {
        e.preventDefault();
        axios.post(API_URL, studentData).then(() => {
            props.resetState();
            props.toggle();
        });
    };

    const editStudent = (e) => {
        e.preventDefault();
        axios.put(API_URL + studentData.pk, studentData).then(() => {
            props.resetState();
            props.toggle();
        });
    };

    const defaultIfEmpty = (value) => {
        return value === '' ? '' : value;
    };

    return (
        <Form onSubmit={props.student ? editStudent : createStudent}>
            <FormGroup>
                <Label for="name">Name:</Label>
                <Input
                    type="text"
                    name="name"
                    onChange={onChange}
                    value={defaultIfEmpty(studentData.name)}
                />
            </FormGroup>
            <FormGroup>
                <Label for="email">Email:</Label>
                <Input
                    type="email"
                    name="email"
                    onChange={onChange}
                    value={defaultIfEmpty(studentData.email)}
                />
            </FormGroup>
            <FormGroup>
                <Label for="document">Document:</Label>
                <Input
                    type="text"
                    name="document"
                    onChange={onChange}
                    value={defaultIfEmpty(studentData.document)}
                />
            </FormGroup>
            <FormGroup>
                <Label for="phone">Phone:</Label>
                <Input
                    type="text"
                    name="phone"
                    onChange={onChange}
                    value={defaultIfEmpty(studentData.phone)}
                />
            </FormGroup>
            <Button>Send</Button>
        </Form>
    );
};

export default NewStudentForm;
