import React, {useState, useEffect} from 'react'
import ListItem from '../components/ListItem'


const SetsListPage = () => {
  // set - LegoSet
  let [sets, setSets] = useState([])

  useEffect(() => {
      getNotes()
  }, [])

  let getNotes = async () => {
    let response = await fetch("/api/sets/", {
      method: 'GET',
      headers: {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3OTAxODk3LCJpYXQiOjE2Njc4MTU0OTcsImp0aSI6IjQyNjhlYWEyNzZmZTQyY2VhMjdmNzU4MDIzMzU0MjM3IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJ0aWtob24iLCJpbWdfZmlsZXBhdGgiOm51bGx9.GM9kauhyf9ezyfX4CrXXYhsb54_vzD3RAsBpnv8V9HE"
      },
    })
    let data = await response.json()
    // console.log(data)
    setSets(data)
  }

  return (
    <div>
      <div className='sets-list'>
        {sets.map((set, index) => (
          <ListItem key={index} set={set} />
        ))}
      </div>
    </div>
  )
}

export default SetsListPage

