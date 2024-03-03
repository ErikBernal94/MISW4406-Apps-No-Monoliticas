CREATE TABLE contratos(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'Llave primaria',
    estado_contrato VARCHAR(255),
    tipo_contrato VARCHAR(255)
) COMMENT 'Tabla base de contratos';
