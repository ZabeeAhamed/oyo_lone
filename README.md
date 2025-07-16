# 🏨 OYO Clone – Hotel Booking Platform (Django)

This project is a clone of the popular hotel booking platform **OYO**, built using **Django** as the backend framework. It simulates key features of a hotel reservation system including user authentication, hotel listings, booking system, and role-based dashboards for customers and vendors.

---

## 🚀 Features

### 👤 User Roles
- **Customer** – Can register, browse hotels, make bookings, and view their booking history.
- **Hotel Vendor** – Can register as a vendor, list hotels, view bookings for their hotels.
- **Admin** – Manages hotel users, vendors, and has full access via Django Admin.

### 🏨 Hotels
- Hotel listing with name, description, images, amenities, and location
- Slug-based URL routing for hotel detail pages
- Hotel Images and multiple Ameneties support
- Offer price vs original price

### 📅 Booking System
- Hotel booking with start and end dates
- Booking tied to both user and hotel
- Booking management by hotel vendors

### 🔐 Authentication
- Custom user models for HotelUser and HotelVendor
- OTP verification during registration (extendable)
- Secure login/logout flow using Django’s auth system

### 🖥️ Dashboards
- Separate dashboards for customer and vendor
- Vendors can view bookings for their hotel(s)

---

## 🛠️ Tech Stack

- **Backend:** Django 5.2, PostgreSQL
- **Frontend:** HTML, CSS (Bootstrap can be integrated)
- **Media & Static:** Image uploads for hotels and profiles
- **Authentication:** Django built-in auth with custom user extensions

---
