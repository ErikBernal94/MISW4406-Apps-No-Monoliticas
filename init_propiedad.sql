CREATE TABLE propiedades(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Llave primaria',
    descripcion_propiedad VARCHAR(255),
    tipo_propiedad VARCHAR(255)
) COMMENT 'Tabla base de propiedades';