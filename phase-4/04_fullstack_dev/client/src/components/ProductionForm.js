import React, {useState} from 'react'
import styled from 'styled-components'
import { useHistory } from 'react-router-dom'
// 6.✅ Verify formik and yet have been added to our package.json dependencies 
// import the useFormik hook from formik
// import * as yup for yup
import {useFormik} from 'formik'
import * as yup from 'yup'


function ProductionForm({addProduction}) {
  const [errors, setErrors] = useState([]);

  const history = useHistory()
  // 7.✅ Use yup to create client side validations
  const productionSchema = yup.object().shape({
    title: yup.string()
      .min(3, 'Title must be at least 3 characters')
      .max(50, 'Title must be at most 50 characters')
      .required('Title is required'),
    genre: yup.string()
      .oneOf(['Drama', 'Musical', 'Opera'])
      .required('Genre is required'),
    budget: yup.number()
      .positive('Budget must be a positive number')
      .max(1000000000, 'Budget must be less than 1 billion')
      .required('Budget is required'),
    image: yup.string()
      .test('is-url', 'Image must be a valid URL', (value) => {
        const urlRegex = /(http(s?):)([/|.|\w|\s|-])*\.(?:jpg|jpeg|png)/g;
        return urlRegex.test(value);
      })
      .required('Image is required'),
    director: yup.string()
      .test('at-least-two-words', 'Title must contain at least two words', (value) => {
        const wordCountRegex = /\b\w+\b/g;
        const words = value ? value.match(wordCountRegex) || [] : [];
        return words.length >= 2;
      })
      .required('Director is required'),
    description: yup.string()
      .min(10, 'Description must be at least 10 characters')
      .max(1000, 'Description must be at most 1000 characters')
      .required('Description is required'),
    ongoing: yup.boolean().required('Ongoing is required')
  })


  // 8.✅ useFormik hook
  const formik = useFormik({
    initialValues: {
      title: '',
      genre: '',
      budget: 'test',
      image: '',
      director: '',
      description: '',
      ongoing: false
    },
    validationSchema: productionSchema,
    onSubmit: (values, {resetForm}) => {
      fetch('/api/v1/productions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(values, null, 2)
      })
      .then(res => {
        if (res.ok) {
          res.json().then(data => {
            addProduction(data)
            resetForm({values: ''})
            history.push('/')
          })
        } else {
          res.json().then(error => setErrors(error.message))
        }
      })
      .catch(err => console.log(err))
    }
  })
  const resetErrors = () => {
    setTimeout(() => {
      // formik.setTouched({});
      formik.setErrors({});
    }, 6000); // Adjust the timeout duration as needed
  };

  // 9.✅ Create a form with the following fields:
    return (
      <div className='App'>
        <p className="errors">{errors}</p>
        <Form onSubmit={formik.handleSubmit}>
          <label>Title </label>
          <input type='text' name='title' value={formik.values.title} onChange={formik.handleChange} />
          {formik.errors.title ? <div className="error-message show">{formik.errors.title}</div> : null}
          <label> Genre</label>
          <input type='text' name='genre' value={formik.values.genre} onChange={formik.handleChange} />
          {formik.errors.genre ? <div className="error-message show">{formik.errors.genre}</div> : null}
          <label>Budget</label>
          <input type='number' name='budget' value={formik.values.budget} onChange={formik.handleChange} />
          {formik.errors.budget ? <div className="error-message show">{formik.errors.budget}</div> : null}
          <label>Image</label>
          <input type='text' name='image'  value={formik.values.image} onChange={formik.handleChange} />
          {formik.errors.image ? <div className="error-message show">{formik.errors.image}</div> : null}
          <label>Director</label>
          <input type='text' name='director' value={formik.values.director} onChange={formik.handleChange} />
          {formik.errors.director ? <div className="error-message show">{formik.errors.director}</div> : null}
          <label>Description</label>
          <textarea type='text' rows='4' cols='50' name='description' value={formik.values.description} onChange={formik.handleChange} />
          {formik.errors.description ? <div className="error-message show">{formik.errors.description}</div> : null}
          <input type='submit' />
        </Form> 
      </div>
    )
  }
  
  export default ProductionForm

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