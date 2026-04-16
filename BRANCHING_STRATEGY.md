# Estructura de Ramas - Taller Formularios Django

## 📊 Estado Actual del Proyecto

```
main (PRODUCCIÓN)
 └── Solo merges autorizados - ESTABLE
 
dev (DESARROLLO)
 ├── feature/solicitudes (MERGED ✓)
 └── Ready para nuevas features
```

## 🎯 Ramas Activas

### `main` 
- **Estado**: Producción estable
- **Último commit**: `0924de1` - Merge pull request #1
- **Acceso**: Solo merges desde `dev` cuando esté autorizado
- **Responsabilidad**: Código probado y validado

### `dev`
- **Estado**: Rama de desarrollo activa
- **Último commit**: `7a70ccc` - config(solicitudes)
- **Acceso**: Recibe merges de ramas feature
- **Responsabilidad**: Integración de nuevas funcionalidades

### `feature/solicitudes` 
- **Estado**: ✅ MERGED a `dev`
- **Commits realizados**:
  1. `fbf47d7` - feat(solicitudes): crear aplicación Django con modelo, formulario y vistas
  2. `7a70ccc` - config(solicitudes): integrar aplicación en settings y urls del proyecto
- **Incluye**: Modelo, formulario, vistas, plantillas, admin, validaciones

---

## 📝 Commits en `feature/solicitudes`

### Commit 1: Aplicación Django
```
feat(solicitudes): crear aplicación Django con modelo, formulario y vistas

- Crear aplicación 'solicitudes' en Django
- Implementar modelo Solicitud con 9 campos
- Agregar validaciones personalizadas
- Crear ModelForm 'SolicitudForm' con widgets Bootstrap 5
- Implementar validaciones a nivel de formulario
- Crear vistas: solicitud_crear y solicitud_confirmacion
- Configurar manejo de errores y mensajes
```

### Commit 2: Configuración del Proyecto
```
config(solicitudes): integrar aplicación en settings y urls del proyecto

- Registrar 'solicitudes' en INSTALLED_APPS
- Configurar rutas en urls.py
- Agregar soporte MEDIA_URL y MEDIA_ROOT
- Integrar gestión de archivos media en desarrollo
```

---

## 🔄 Flujo de Trabajo

```
1. Crear rama feature desde dev
   git checkout dev
   git checkout -b feature/nueva-funcionalidad

2. Desarrollar en la rama feature
   git add .
   git commit -m "descriptive message"

3. Mergear a dev cuando esté lista
   git checkout dev
   git merge feature/nueva-funcionalidad

4. Cuando dev esté lista para producción
   git checkout main
   git merge dev
   (SOLO CUANDO LO INDIQUE)
```

---

## 📦 Contenido de `feature/solicitudes`

### Archivos Creados:
- `solicitudes/models.py` - Modelo Solicitud con validaciones
- `solicitudes/forms.py` - ModelForm con widgets Bootstrap 5
- `solicitudes/views.py` - Vistas de creación y confirmación
- `solicitudes/urls.py` - Rutas de la aplicación
- `solicitudes/admin.py` - Configuración del admin
- `solicitudes/templates/solicitudes/solicitud_form.html` - Formulario responsivo
- `solicitudes/templates/solicitudes/confirmacion.html` - Página de éxito
- `solicitudes/migrations/0001_initial.py` - Migración inicial

### Archivos Modificados:
- `taller_formularios/settings.py` - Agregada app + MEDIA config
- `taller_formularios/urls.py` - Integradas URLs de solicitudes

---

## ✅ Validación

### Campos del Modelo:
✓ Nombre solicitante (max 150 caracteres)
✓ Documento de identidad (alfanumérico)
✓ Correo electrónico (validación email)
✓ Teléfono (validación de formato)
✓ Tipo de solicitud (select: académica, administrativa, técnica, otra)
✓ Asunto (max 200 caracteres)
✓ Descripción detallada (TextField)
✓ Fecha de solicitud (auto_now_add)
✓ Archivo adjunto (opcional, con validación de tipos)

---

## 🚀 Próximos Pasos

1. **Cuando todo esté listo**: Yo indicaré cuándo mergear `dev` → `main`
2. **Nueva funcionalidad**: Crear nueva rama `feature/` desde `dev`
3. **Testing**: Verificar en `dev` antes de mergear a `main`

---

## 📌 Convención de Commits

```
feat(modulo): descripción breve
- Detalle 1
- Detalle 2

config(modulo): descripción breve
- Cambio 1
- Cambio 2

fix(modulo): descripción del fix
```

---

**Generado**: 16 de abril de 2026
**Dev Responsable**: Developer 2 (Solicitudes)
