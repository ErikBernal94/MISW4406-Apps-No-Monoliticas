CREATE TABLE contratos(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Llave primaria',
    estado VARCHAR(255),
    tipo VARCHAR(255)
) COMMENT 'Tabla base de contratos';
