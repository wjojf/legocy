import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom';

const SetPage = () => {
    
    let {setId} = useParams();
  
    let [set, setSet] = useState(null)
    useEffect(() => {
        getSet()
    }, null)

    let getSet = async () => {
        let response = await fetch(`/api/sets/${setId}/`, {
            method: 'GET',
            headers: {
              "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3OTAxODk3LCJpYXQiOjE2Njc4MTU0OTcsImp0aSI6IjQyNjhlYWEyNzZmZTQyY2VhMjdmNzU4MDIzMzU0MjM3IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJ0aWtob24iLCJpbWdfZmlsZXBhdGgiOm51bGx9.GM9kauhyf9ezyfX4CrXXYhsb54_vzD3RAsBpnv8V9HE"
            }
        })
        let data = await response.json()
        setSet(data)
    }

    return (
    <div>
      <p>{set?.set_number} {set?.title}: {set?.series.name}</p>
    </div>
  )
}

export default SetPage
