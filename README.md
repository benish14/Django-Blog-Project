Django Blog Platform

Secure Authentication · Role-Based Access · Clean Architecture

A robust and secure blog management platform built using Django and MySQL, engineered with a strong emphasis on authentication workflows, authorization controls, and protected resource access. This project demonstrates real-world backend development practices and security-focused design.

🚀 Project Highlights

Production-style authentication and authorization flow

Protected routes preventing unauthorized and direct URL access

Secure password recovery using email-based token validation

Modular and scalable Django project architecture

Customized admin experience for efficient data control

🧠 Core Functionality
Authentication & Authorization

User registration, login, and logout

Secure password reset via email with time-bound tokens

Session-based authentication using Django’s built-in framework

Role-based authorization restricting sensitive actions

Access Control & Security

Dashboard access limited to authenticated users only

Direct URL access prevention using custom middleware

CSRF protection and server-side form validation

Secure password hashing and session management

Blog Management

Create, update, and delete blog posts

Authenticated user-only post creation

Structured CRUD operations with permission checks

Admin Customization

Customized Django Admin models

Optimized admin views for managing users and posts

Improved usability and data visibility

🏗️ Architecture Overview

The application follows Django’s recommended MVC architecture, ensuring maintainability and scalability.
