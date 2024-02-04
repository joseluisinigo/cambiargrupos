import os
import pwd
import grp
import shutil

def cambiar_propiedades(ruta, usuario_archivos, grupo_archivos, usuario_carpetas, grupo_carpetas):
    confirmacion1 = input(f"¿Estás seguro de cambiar las propiedades de los archivos y carpetas en '{ruta}'? (Escribe 'si quiero cambiar los permisos' para confirmar): ")
    
    if confirmacion1.lower() != 'si quiero cambiar los permisos':
        print("Operación cancelada.")
        return
    
    for root, dirs, files in os.walk(ruta):
        for dir in dirs:
            carpeta = os.path.join(root, dir)
            try:
                uid = pwd.getpwnam(usuario_carpetas).pw_uid
                gid = grp.getgrnam(grupo_carpetas).gr_gid
                os.chown(carpeta, uid, gid)
                print(f"Cambiando propiedades de la carpeta '{carpeta}' a usuario '{usuario_carpetas}' y grupo '{grupo_carpetas}'")
            except (FileNotFoundError, PermissionError) as e:
                print(f"No se pudo cambiar las propiedades de la carpeta '{carpeta}': {str(e)}")
        
        for file in files:
            archivo = os.path.join(root, file)
            try:
                uid = pwd.getpwnam(usuario_archivos).pw_uid
                gid = grp.getgrnam(grupo_archivos).gr_gid
                os.chown(archivo, uid, gid)
                print(f"Cambiando propiedades del archivo '{archivo}' a usuario '{usuario_archivos}' y grupo '{grupo_archivos}'")
            except (FileNotFoundError, PermissionError) as e:
                print(f"No se pudo cambiar las propiedades del archivo '{archivo}': {str(e)}")

if __name__ == "__main__":
    ruta_actual = os.getcwd()
    print(f"Esta acción cambiará las propiedades de los archivos y carpetas en la ruta: {ruta_actual}")
    
    usuario_archivos = input("Por favor, introduce el nombre de usuario para archivos: ")
    grupo_archivos = input("Por favor, introduce el nombre del grupo para archivos: ")
    
    misma_propiedad = input("¿Deseas utilizar los mismos usuarios y grupos para archivos y carpetas? (s/n): ")
    
    if misma_propiedad.lower() == 'n':
        usuario_carpetas = input("Por favor, introduce el nombre de usuario para carpetas: ")
        grupo_carpetas = input("Por favor, introduce el nombre del grupo para carpetas: ")
    else:
        usuario_carpetas = usuario_archivos
        grupo_carpetas = grupo_archivos
    
    confirmacion2 = input("¿Estás seguro de cambiar las propiedades con las siguientes configuraciones? (Escribe 'si quiero cambiar los permisos' para confirmar):\n"
                         f"Usuario para archivos: {usuario_archivos}\n"
                         f"Grupo para archivos: {grupo_archivos}\n"
                         f"Usuario para carpetas: {usuario_carpetas}\n"
                         f"Grupo para carpetas: {grupo_carpetas}\n")
    
    if confirmacion2.lower() == 'si quiero cambiar los permisos':
        cambiar_propiedades(ruta_actual, usuario_archivos, grupo_archivos, usuario_carpetas, grupo_carpetas)
        print("Operación completada.")
    else:
        print("Operación cancelada.")
