// Simulación de base de datos de usuarios
let users = JSON.parse(localStorage.getItem('users')) || [];

// Función para registrar un nuevo usuario
function registerUser(name, email, username, password) {
    // Verificar si el usuario ya existe
    const existingUser = users.find(user => user.username === username || user.email === email);
    if (existingUser) {
        return { success: false, message: 'El usuario o email ya está registrado' };
    }
    
    // Crear nuevo usuario (en un caso real, aquí se haría hash de la contraseña)
    const newUser = {
        id: Date.now().toString(),
        name,
        email,
        username,
        password, // ¡En producción nunca almacenes contraseñas en texto plano!
        createdAt: new Date().toISOString()
    };
    
    users.push(newUser);
    localStorage.setItem('users', JSON.stringify(users));
    
    return { success: true, user: newUser };
}

// Función para autenticar usuario
function loginUser(username, password) {
    const user = users.find(user => 
        (user.username === username || user.email === username) && 
        user.password === password
    );
    
    if (!user) {
        return { success: false, message: 'Usuario o contraseña incorrectos' };
    }
    
    // Almacenar usuario actual (en un caso real usarías sesiones o tokens JWT)
    localStorage.setItem('currentUser', JSON.stringify(user));
    
    return { success: true, user };
}

// Manejar formulario de registro
if (document.getElementById('registerForm')) {
    document.getElementById('registerForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const name = document.getElementById('registerName').value;
        const email = document.getElementById('registerEmail').value;
        const username = document.getElementById('registerUsername').value;
        const password = document.getElementById('registerPassword').value;
        const confirmPassword = document.getElementById('registerConfirmPassword').value;
        
        // Validaciones básicas
        if (password !== confirmPassword) {
            document.getElementById('registerMessage').textContent = 'Las contraseñas no coinciden';
            return;
        }
        
        if (password.length < 8) {
            document.getElementById('registerMessage').textContent = 'La contraseña debe tener al menos 8 caracteres';
            return;
        }
        
        const result = registerUser(name, email, username, password);
        
        if (result.success) {
            // Registro exitoso, redirigir a dashboard
            localStorage.setItem('currentUser', JSON.stringify(result.user));
            window.location.href = 'dashboard.html';
        } else {
            document.getElementById('registerMessage').textContent = result.message;
        }
    });
}

// Manejar formulario de login
if (document.getElementById('loginForm')) {
    document.getElementById('loginForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const username = document.getElementById('loginUsername').value;
        const password = document.getElementById('loginPassword').value;
        
        const result = loginUser(username, password);
        
        if (result.success) {
            // Login exitoso, redirigir a dashboard
            window.location.href = 'dashboard.html';
        } else {
            document.getElementById('loginMessage').textContent = result.message;
        }
    });
}

// Verificar autenticación al cargar páginas protegidas
function checkAuth() {
    const protectedPages = ['dashboard.html'];
    const currentPage = window.location.pathname.split('/').pop();
    
    if (protectedPages.includes(currentPage)) {
        const user = JSON.parse(localStorage.getItem('currentUser'));
        if (!user) {
            window.location.href = 'login.html';
        }
    }
}

// Ejecutar verificación al cargar la página
document.addEventListener('DOMContentLoaded', checkAuth);