1. Partiendo del modelo creado en el CUE anterior, releacionado al modelo de fabrica y productos, liste todas las migraciones realizadas e indique por qué se crea el archivo 001_inicial.py
`python manage.py showmigrations`
2. ¿Cuál es el comando que permite observa el SQL antes de aplicar una determinada migracion, por ejemplo la 0001_inicial.py?
`python manage.py sqlmigrate <app> <migration_number>`
`python manage.py sqlmigrate producto 0001`
3. ¿Cuáles son las claves primarias de los modelos?
('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
