CREATE TABLE propiedades(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Llave primaria',
    nombres VARCHAR(255),
    direccion VARCHAR(255)
) COMMENT 'Tabla base de propiedades';