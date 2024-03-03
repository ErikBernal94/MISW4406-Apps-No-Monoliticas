CREATE TABLE companias(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Llave primaria',
    correo_electronico VARCHAR(255),
    direccion VARCHAR(255)
) COMMENT 'Tabla base de companias';
