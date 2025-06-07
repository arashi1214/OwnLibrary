import React from 'react'
import { redirect } from 'react-router-dom'

import Button from '@mui/material/Button';

let url = 'https://127.0.0.1:8000'

const AddBook = () => {
    function addData(url, data){
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
            redirect: 'follow',
        }



        fetch('${url}/create_book', requestOptions)
        .then((response) => response.json())
        .then((result) => {
            console.log(result)
            getFormData()
        })
        .catch((error) => console.log('error', error))
    }

    function getFormData(){

    }



    return (
        <div>
            <form>
                <input type='txet' name='title' placeholder='書名' required></input>
                <input type='txet' name='author' placeholder='作者'></input>
                <input type='txet' name='isbn' placeholder='ISBN'></input>
                <input type='txet' name='category' placeholder='類型'></input>
                <input type='number' name='price' placeholder='價格'></input>
                <Button variant="contained" onClick={ ()=>{addData(url)}}>新增</Button>
            </form>
        </div>
      )
}





AddBook.propTypes = {}
export default AddBook
