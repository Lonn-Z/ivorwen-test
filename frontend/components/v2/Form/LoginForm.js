// frontend/components/v2/Form/LoginForm.js
import React from 'react';

export default function LoginForm() {
    return (
        <form className="flex flex-col space-y-2.5">
            <input type="text" placeholder="Username" className="border p-2" />
            <input type="password" placeholder="Password" className="border p-2" />
            <button type="submit" className="bg-blue-500 text-white p-2 rounded">Login</button>
        </form>
    );
}
