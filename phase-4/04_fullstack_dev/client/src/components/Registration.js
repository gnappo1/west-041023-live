import React, { useState } from 'react'
import { useHistory } from 'react-router-dom'
import {useFormik} from 'formik'
import * as yup from 'yup'
import styled from 'styled-components'

const Registration = ({updateCurrentUser, addError}) => {
    const [isLogin, setIsLogin] = useState(false)
    const history = useHistory()

    const userSchema = yup.object().shape({
        username: yup.string()
            .min(8, "Username must be at least 8 characters")
            .max(20, "Username must be at most 20 characters")
            .test("valid-chs", 
                    "Username may only contain letters and numbers", 
                    (value) => {
                        return /^[A-z0-9]+$/.test(value);
                    })
            .required("Username is required"),
        email: yup.string()
            .email("Email must be valid")
            .required("Email is required"),
        password: yup.string()
            .min(10, "Password must be at least 10 characters")
            .test("valid-chs", 
                "Password should have at least one uppercase letter, one lowercase letter, one number, and one special character", 
                (value) => {
                    return /[A-Z]/.test(value) && /[^A-Za-z0-9]/.test(value) && /[a-z]/.test(value) && /[0-9]/.test(value)
                })
            .required("Password is required"),
        password_confirmation: yup.string()
            .oneOf([yup.ref('password'), null], "Passwords must match")
            .required("Password confirmation is required")
    })

    const formik = useFormik({
        initialValues: {
            username: "",
            email: "",
            password: "",
            password_confirmation: ""
        },
        validationSchema: isLogin ? null : userSchema,
        onSubmit: (values) => {
            debugger
            const endpoint = isLogin ? "/api/v1/signin" : "/api/v1/signup"
            const data = isLogin ? {email: values.email, password_hash: values.password} : {...values, password_hash: values.password}

            fetch(endpoint, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            })
            .then(res => {
                if (res.ok) {
                    res.json()
                    .then(data => {
                        localStorage.setItem('token', data.token)
                        localStorage.setItem('refreshToken', data.refresh_token)
                        updateCurrentUser(data.user)
                    })
                    .then(() => history.push("/"))
                } else {
                    res.json()
                    .then(err => addError(err.error))
                }
            })
        }
    })


    return (
        <div style={{textAlign: "center"}}>
            <Form onSubmit={formik.handleSubmit}>
                {isLogin ? null : <>
                    <label>Username </label>
                    <input type='text' name='username' value={formik.values.username} onChange={formik.handleChange} onBlur={formik.handleBlur}/>
                    {formik.errors.username && formik.touched.username ? <div className="error-message show">{formik.errors.username}</div> : null}
                </>}
                <label>Email</label>
                <input type='email' name='email' value={formik.values.email} onChange={formik.handleChange} onBlur={formik.handleBlur}/>
                {formik.errors.email && formik.touched.email ? <div className="error-message show">{formik.errors.email}</div> : null}
                <label>Password</label>
                <input type='password' name='password' value={formik.values.password} onChange={formik.handleChange} onBlur={formik.handleBlur}/>
                {formik.errors.password && formik.touched.password ? <div className="error-message show">{formik.errors.password}</div> : null}
                {isLogin ? null : <>
                    <label>Password Confirmation</label>
                    <input type='password' name='password_confirmation'  value={formik.values.password_confirmation} onChange={formik.handleChange} onBlur={formik.handleBlur}/>
                    {formik.errors.password_confirmation && formik.touched.password_confirmation ? <div className="error-message show">{formik.errors.password_confirmation}</div> : null}
                </>}
                <input type='submit' value={isLogin ? "Login" : "Create"}/>
            </Form>
            <Span>{isLogin ? "Need a new account?" : "Already have an account?"}<button onClick={() => setIsLogin(!isLogin)}>{isLogin ? "Create" : "Login"}</button></Span>
        </div>
    )
}

export default Registration

const Form = styled.form`
    display:flex;
    flex-direction:column;
    width: 400px;
    margin:auto;
    font-family:Arial;
    font-size:30px;
    input[type=submit]{
        background-color:#42ddf5;
        color: white;
        height:40px;
        font-family:Arial;
        font-size:30px;
        margin-top:10px;
        margin-bottom:10px;
    }
`

const Span = styled.span`
    font-family:Arial;
    font-size:30px;
    text-align:center;
    button{
        background-color:#42ddf5;
        color: white;
        height:40px;
        font-family:Arial;
        font-size:30px;
        margin-top:10px;
        margin-bottom:10px;
    };
    button:hover{
        height:45px;
    };
`