import React, { useState, useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import { NavLink } from "react-router-dom";
import './Navigation.css'

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
  };

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");
  const closeMenu = () => setShowMenu(false);

  return (
    <>
    <div className="sign-in-and-cart">
      <button onClick={openMenu} className='sign-in-home'>
        <i className="fas fa-user-circle" />
      </button>
      <NavLink exact to={`/cart`} className='cart-icon'>
        <i className="fas fa-shopping-cart" />
			</NavLink>
    </div>
      <ul className={ulClassName} ref={ulRef}>
        {user ? (
          <>
            <div>{user.username}</div>
            <div>{user.email}</div>
            <div className="booking-icon">
              <NavLink exact to={`/bookings`} className='icon'>
                Schedule a booking
              </NavLink>
            </div>
            <div className="my-bookings">
              <NavLink exact to={`/myBookings`} className='icon'>
                My Bookings
              </NavLink>
            </div>
            {/* <div className="my-favorites">
              <NavLink exact to={`/myFavorites`} className='icon'>
                My Favorites
              </NavLink>
            </div> */}
            <div>
              <button className="logoutbutton" onClick={handleLogout}>Log Out</button>
            </div>
          </>
        ) : (
          <>
            <OpenModalButton
              buttonText="Log In"
              onItemClick={closeMenu}
              modalComponent={<LoginFormModal />}
            />

            <OpenModalButton
              buttonText="Sign Up"
              onItemClick={closeMenu}
              modalComponent={<SignupFormModal />}
            />
          </>
        )}
      </ul>
    </>
  );
}

export default ProfileButton;
