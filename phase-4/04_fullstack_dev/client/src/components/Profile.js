import React from 'react'

const Profile = ({currentUser}) => {
    return (
        <div>
            <h2>Welcome back {currentUser.username}</h2>
            <br />
            <button>Edit Account</button>
            <button>Delete Account</button>
        </div>
    )
}

export default Profile