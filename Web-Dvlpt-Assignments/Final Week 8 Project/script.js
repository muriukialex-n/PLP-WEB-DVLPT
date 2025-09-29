// NOTE: This is a front-end simulation. In production, replace with actual API calls to your backend.

// Simulated database using in-memory storage (replaces localStorage for compatibility)
let database = {
  users: [
    {
      user_id: 1,
      username: 'admin',
      email: 'admin@hotel.com',
      password: 'admin123', // In production, this would be hashed
      full_name: 'System Administrator',
      phone: '+254123456789',
      user_type: 'admin'
    }
  ],
  rooms: [
    { room_id: 1, room_number: '101', room_type: 'Single', price_per_night: 50, capacity: 1, description: 'Cozy single room', amenities: 'WiFi, TV, AC', status: 'available' },
    { room_id: 2, room_number: '102', room_type: 'Single', price_per_night: 50, capacity: 1, description: 'Comfortable single room', amenities: 'WiFi, TV, AC', status: 'available' },
    { room_id: 3, room_number: '201', room_type: 'Double', price_per_night: 80, capacity: 2, description: 'Spacious double room', amenities: 'WiFi, TV, AC, Mini Bar', status: 'available' },
    { room_id: 4, room_number: '202', room_type: 'Double', price_per_night: 80, capacity: 2, description: 'Modern double room', amenities: 'WiFi, TV, AC, Mini Bar', status: 'available' },
    { room_id: 5, room_number: '301', room_type: 'Suite', price_per_night: 120, capacity: 4, description: 'Luxury suite', amenities: 'WiFi, TV, AC, Mini Bar, Balcony, Jacuzzi', status: 'available' },
    { room_id: 6, room_number: '302', room_type: 'Suite', price_per_night: 120, capacity: 4, description: 'Premium suite', amenities: 'WiFi, TV, AC, Mini Bar, Balcony, Jacuzzi', status: 'available' },
    { room_id: 7, room_number: '401', room_type: 'Deluxe', price_per_night: 150, capacity: 3, description: 'Deluxe room', amenities: 'WiFi, TV, AC, Mini Bar, Balcony', status: 'available' }
  ],
  bookings: [],
  currentUser: null,
  nextBookingId: 1,
  nextRoomId: 8,
  nextUserId: 2
};

// Current booking session
let currentBooking = {
  room: null,
  checkIn: null,
  checkOut: null,
  nights: 0
};

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  initializeEventListeners();
  setMinDate();
});

// Event Listeners
function initializeEventListeners() {
  // Auth tabs
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => switchAuthTab(btn.dataset.tab));
  });

  // Forms
  document.getElementById('registerForm').addEventListener('submit', handleRegister);
  document.getElementById('loginForm').addEventListener('submit', handleLogin);
  document.getElementById('logoutBtn').addEventListener('click', handleLogout);
  
  // Room search and booking
  document.getElementById('searchRooms').addEventListener('click', searchAvailableRooms);
  document.getElementById('roomForm').addEventListener('submit', handleBookingSubmit);
  document.getElementById('paymentForm').addEventListener('submit', handlePayment);
  
  // Cancel buttons
  document.getElementById('cancelBooking')?.addEventListener('click', () => {
    showSection('room-selection');
  });
  document.getElementById('cancelPayment')?.addEventListener('click', () => {
    showSection('booking-form');
  });
  document.getElementById('backToRooms')?.addEventListener('click', () => {
    showSection('room-selection');
  });

  // Admin functionality
  document.querySelectorAll('.admin-tab-btn').forEach(btn => {
    btn.addEventListener('click', () => switchAdminTab(btn.dataset.tab));
  });
  
  document.getElementById('showAddRoom')?.addEventListener('click', () => {
    document.getElementById('add-room-form').style.display = 'block';
  });
  
  document.getElementById('cancelAddRoom')?.addEventListener('click', () => {
    document.getElementById('add-room-form').style.display = 'none';
    document.getElementById('addRoomForm').reset();
  });
  
  document.getElementById('addRoomForm')?.addEventListener('submit', handleAddRoom);
  document.getElementById('filterBookings')?.addEventListener('click', filterBookings);
}

// Set minimum date for date inputs
function setMinDate() {
  const today = new Date().toISOString().split('T')[0];
  document.getElementById('check-in').setAttribute('min', today);
  document.getElementById('check-out').setAttribute('min', today);
  
  document.getElementById('check-in').addEventListener('change', (e) => {
    const checkIn = new Date(e.target.value);
    checkIn.setDate(checkIn.getDate() + 1);
    document.getElementById('check-out').setAttribute('min', checkIn.toISOString().split('T')[0]);
  });
}

// Switch Authentication Tab
function switchAuthTab(tab) {
  document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
  document.querySelectorAll('.auth-form').forEach(form => form.classList.remove('active'));
  
  document.querySelector(`[data-tab="${tab}"]`).classList.add('active');
  document.getElementById(`${tab}-form`).classList.add('active');
}

// Switch Admin Tab
function switchAdminTab(tab) {
  document.querySelectorAll('.admin-tab-btn').forEach(btn => btn.classList.remove('active'));
  document.querySelectorAll('.admin-panel').forEach(panel => panel.classList.remove('active'));
  
  document.querySelector(`[data-tab="${tab}"]`).classList.add('active');
  document.getElementById(tab).classList.add('active');
  
  if (tab === 'manage-rooms') {
    displayRoomsManagement();
  } else if (tab === 'view-bookings') {
    displayAllBookings();
  }
}

// Registration
function handleRegister(e) {
  e.preventDefault();
  
  const fullName = document.getElementById('reg-fullname').value.trim();
  const username = document.getElementById('reg-username').value.trim();
  const email = document.getElementById('reg-email').value.trim();
  const phone = document.getElementById('reg-phone').value.trim();
  const password = document.getElementById('reg-password').value;
  const confirmPassword = document.getElementById('reg-confirm-password').value;
  
  // Validation
  if (password !== confirmPassword) {
    showNotification('Passwords do not match!', 'error');
    return;
  }
  
  if (password.length < 6) {
    showNotification('Password must be at least 6 characters!', 'error');
    return;
  }
  
  // Check if username or email already exists
  if (database.users.some(u => u.username === username)) {
    showNotification('Username already exists!', 'error');
    return;
  }
  
  if (database.users.some(u => u.email === email)) {
    showNotification('Email already registered!', 'error');
    return;
  }
  
  // Create new user
  const newUser = {
    user_id: database.nextUserId++,
    username,
    email,
    password, // In production, hash this password
    full_name: fullName,
    phone,
    user_type: 'customer'
  };
  
  database.users.push(newUser);
  
  // Send welcome email (simulated)
  sendEmail(email, 'welcome', { name: fullName });
  
  showNotification('Registration successful! Please login.', 'success');
  document.getElementById('registerForm').reset();
  switchAuthTab('login');
}

// Login
function handleLogin(e) {
  e.preventDefault();
  
  const username = document.getElementById('login-username').value.trim();
  const password = document.getElementById('login-password').value;

  // Find user
  const user = database.users.find(u => u.username === username && u.password === password);
  if (!user) {
    showNotification('Invalid username or password!', 'error');
    return;
  }

  database.currentUser = user;

  showNotification(`Welcome, ${user.full_name}!`, 'success');
  document.getElementById('loginForm').reset();

  // Show appropriate section
  if (user.user_type === 'admin') {
    showSection('admin-dashboard');
    switchAdminTab('manage-rooms');
  } else {
    showSection('room-selection');
  }
}