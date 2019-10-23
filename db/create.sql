CREATE DATABASE `soc_taller3`;

use soc_taller3;

CREATE TABLE `personas` (
  `cedula` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `actividad` varchar(45) NOT NULL,
  `estrato` int(11) NOT NULL,
  `foto` varchar(200) NOT NULL,
  PRIMARY KEY (`cedula`)
) ;
