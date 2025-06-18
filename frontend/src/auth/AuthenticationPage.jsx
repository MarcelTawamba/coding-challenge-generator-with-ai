import { SignIn, SignUp, SignedIn, SignedOut } from '@clerk/clerk-react'

export default function AuthenticationPage() {
  return <div className="container">
    {/* if user is signed-out then the inner component is rendered */}
    <SignedOut>
      <SignIn routing='path' path='/sign-in' />
      <SignUp routing='path' path='/sign-up' />
    </SignedOut>
    {/* if user is signed-in then the inner component is rendered */}
    <SignedIn>
      <div className='redirect-message'>
        <p>You are already signed in.</p>
      </div>
    </SignedIn>
  </div>
}