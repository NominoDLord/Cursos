```
##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ##      #####   #####   #####  
###  ##  ##   ##  ###  ###    ##    ###  ##  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##
## # ##  ##   ##  ## ## ##    ##    ## # ##  ##   ##      ##   ##      ##     ##   ##  #####   ##   ##
##  ###  ##   ##  ##    ##    ##    ##  ###  ##   ##      ##   ##      ##     ##   ##  ##  ##  ##   ##
##   ##   #####   ##    ##  ######  ##   ##   #####       #####        ######  #####   ##  ##  #####  
```

# .gitignore

---
---

## Introducción

El archivo ***.gitignore*** es un archivo de configuración que se utiliza en repositorios de Git para especificar patrones de archivos y directorios que Git debe ignorar al realizar operaciones de seguimiento y versión.

Esto es útil para evitar que archivos y directorios generados automáticamente, archivos temporales y otros elementos no deseados se incluyan accidentalmente en el control de versiones.


## Funcionamiento básico

1. **Patrones para ignorar archivos**
	- En el archivo .gitignore, puedes especificar patrones de nombres de archivos o directorios que Git debe ignorar.

2. **Formato de los Patrones**
	- Los patrones pueden incluir caracteres especiales como asteriscos (*), barras inclinadas (/), comillas (") y otros para describir patrones de nombres de archivos o directorios.

## ¿Cómo usar .gitignore?

1. **Creación del Archivo**

	- Si tu repositorio aún no tiene un archivo .gitignore, puedes crear uno en la raíz del repositorio.

2. **Editar Archivo**

	- Abre el archivo .gitignore en un editor de texto.
	- Agrega los patrones de archivos y directorios que deseas ignorar.
	
``` .gitignore
# Ignorar archivos temporales
*.tmp

# Ignorar directorios llamados "temp"
temp/
```

3. **Guardar y Hacer Commit**

	- Guarda los cambios en el archivo .gitignore.
	- Realiza un commit para aplicar el archivo .gitignore al repositorio.

4. **Efecto en el Repositorio**

	- Después de agregar un patrón en `.gitignore` y hacer commit, Git ignorará los archivos y directorios que coincidan con esos patrones durante las operaciones de seguimiento y versión.


### Ejemplos de Patrones en .gitignore:

- `*.log`: Ignora todos los archivos con extensión `.log`.

- `node_modules/`: Ignora el directorio node_modules y su contenido.

- `/temp`: Ignora el directorio temp en la raíz del repositorio.

###### Consejos:

- **Comentarios**

	- Puedes agregar comentarios a .gitignore utilizando el símbolo #.

- **Global Gitignore**

	- Además del `.gitignore` local en la raíz del repositorio, puedes tener un archivo de configuración global de gitignore (~/.gitignore_global) que se aplica a todos tus repositorios.

Recuerda que los archivos y directorios ya rastreados por Git antes de agregarlos a `.gitignore` seguirán siendo rastreados.

Para dejar de rastrearlos, puedes usar `git rm --cached` y hacer un commit.

En resumen, `.gitignore` es una herramienta valiosa para personalizar qué archivos y directorios Git debe ignorar, facilitando el control del contenido que se agrega al repositorio.


## ¿Cómo añadir el archivo 'gitignore_global'?

1. Crea el archivo global `.gitignore`

Se puede crear el archivo .gitignore_global en tu directorio de inicio (~) o en cualquier otro lugar que elijas.

Aquí hay un ejemplo que podrías ejecutar en la línea de comandos para crear el archivo:

``` Git Bash
touch ~/.gitignore_global
```

2. Configura Git para usar el archivo global `.gitignore`

Ejecuta el siguiente comando para decirle a Git que use tu archivo .gitignore_global como el archivo de ignorar global:

```Git Bash
git config --global core.excludesfile ~/.gitignore_global
```