-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-07-2024 a las 09:59:33
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `correoyuri`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `area`
--

CREATE TABLE `area` (
  `id_area` int(11) NOT NULL,
  `nombre_area` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carga_familiar`
--

CREATE TABLE `carga_familiar` (
  `id_carga_familiar` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `usuario_id_usuario` int(11) NOT NULL,
  `parentesco_id_parentesco` int(11) NOT NULL,
  `genero_trabajador_id_sexo_usuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargo_trabajador`
--

CREATE TABLE `cargo_trabajador` (
  `id_cargo_trabajador` int(11) NOT NULL,
  `cargo_trabajador` varchar(45) NOT NULL,
  `fecha_ingreso` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contacto_emergencia`
--

CREATE TABLE `contacto_emergencia` (
  `id_contacto_emergencia` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `telefono` int(11) NOT NULL,
  `parentesco_id_parentesco` int(11) NOT NULL,
  `relacion_trabajador` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento`
--

CREATE TABLE `departamento` (
  `id_departamento` int(11) NOT NULL,
  `nombre_departamento` varchar(45) NOT NULL,
  `area_id_area1` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genero_trabajador`
--

CREATE TABLE `genero_trabajador` (
  `id_sexo_usuario` int(11) NOT NULL,
  `sexo` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `parentesco`
--

CREATE TABLE `parentesco` (
  `id_parentesco` int(11) NOT NULL,
  `parentesco` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `rut` varchar(45) NOT NULL,
  `direccion` varchar(45) NOT NULL,
  `telefono` varchar(45) NOT NULL,
  `contraseña` varchar(45) NOT NULL,
  `cargo_trabajador_id_cargo_trabajador` int(11) NOT NULL,
  `genero_trabajador_id_sexo_usuario` int(11) NOT NULL,
  `departamento_id_departamentos` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_has_contacto_emergencia`
--

CREATE TABLE `usuario_has_contacto_emergencia` (
  `id_contacto_usuario` int(11) NOT NULL,
  `contacto_emergencia_id_contacto_emergencia` int(11) NOT NULL,
  `usuario_id_usuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `area`
--
ALTER TABLE `area`
  ADD PRIMARY KEY (`id_area`);

--
-- Indices de la tabla `carga_familiar`
--
ALTER TABLE `carga_familiar`
  ADD PRIMARY KEY (`id_carga_familiar`),
  ADD UNIQUE KEY `carga_familiar_UNIQUE` (`id_carga_familiar`),
  ADD KEY `fk_carga_familiar_usuario1_idx` (`usuario_id_usuario`),
  ADD KEY `fk_carga_familiar_parentesco1_idx` (`parentesco_id_parentesco`),
  ADD KEY `fk_carga_familiar_genero_trabajador1_idx` (`genero_trabajador_id_sexo_usuario`);

--
-- Indices de la tabla `cargo_trabajador`
--
ALTER TABLE `cargo_trabajador`
  ADD PRIMARY KEY (`id_cargo_trabajador`),
  ADD UNIQUE KEY `id_cargo_trabajador_UNIQUE` (`id_cargo_trabajador`);

--
-- Indices de la tabla `contacto_emergencia`
--
ALTER TABLE `contacto_emergencia`
  ADD PRIMARY KEY (`id_contacto_emergencia`),
  ADD UNIQUE KEY `id_contacto_emergencia_UNIQUE` (`id_contacto_emergencia`),
  ADD KEY `fk_contacto_emergencia_parentesco1_idx` (`parentesco_id_parentesco`);

--
-- Indices de la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`id_departamento`),
  ADD UNIQUE KEY `id_departamentos_UNIQUE` (`id_departamento`),
  ADD KEY `fk_departamento_area1_idx` (`area_id_area1`);

--
-- Indices de la tabla `genero_trabajador`
--
ALTER TABLE `genero_trabajador`
  ADD PRIMARY KEY (`id_sexo_usuario`),
  ADD UNIQUE KEY `id_sexo_usuario_UNIQUE` (`id_sexo_usuario`);

--
-- Indices de la tabla `parentesco`
--
ALTER TABLE `parentesco`
  ADD PRIMARY KEY (`id_parentesco`),
  ADD UNIQUE KEY `idparentesco_UNIQUE` (`id_parentesco`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `id_usuario_UNIQUE` (`id_usuario`),
  ADD KEY `fk_usuario_cargo_trabajador_idx` (`cargo_trabajador_id_cargo_trabajador`),
  ADD KEY `fk_usuario_genero_trabajador1_idx` (`genero_trabajador_id_sexo_usuario`),
  ADD KEY `fk_usuario_departamento1_idx` (`departamento_id_departamentos`);

--
-- Indices de la tabla `usuario_has_contacto_emergencia`
--
ALTER TABLE `usuario_has_contacto_emergencia`
  ADD PRIMARY KEY (`id_contacto_usuario`),
  ADD UNIQUE KEY `id_contacto_usuario_UNIQUE` (`id_contacto_usuario`),
  ADD KEY `fk_usuario_has_contacto_emergencia_contacto_emergencia1_idx` (`contacto_emergencia_id_contacto_emergencia`),
  ADD KEY `fk_usuario_has_contacto_emergencia_usuario1_idx` (`usuario_id_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cargo_trabajador`
--
ALTER TABLE `cargo_trabajador`
  MODIFY `id_cargo_trabajador` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `contacto_emergencia`
--
ALTER TABLE `contacto_emergencia`
  MODIFY `id_contacto_emergencia` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `departamento`
--
ALTER TABLE `departamento`
  MODIFY `id_departamento` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `genero_trabajador`
--
ALTER TABLE `genero_trabajador`
  MODIFY `id_sexo_usuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `parentesco`
--
ALTER TABLE `parentesco`
  MODIFY `id_parentesco` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario_has_contacto_emergencia`
--
ALTER TABLE `usuario_has_contacto_emergencia`
  MODIFY `id_contacto_usuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `carga_familiar`
--
ALTER TABLE `carga_familiar`
  ADD CONSTRAINT `fk_carga_familiar_genero_trabajador1` FOREIGN KEY (`genero_trabajador_id_sexo_usuario`) REFERENCES `genero_trabajador` (`id_sexo_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_carga_familiar_parentesco1` FOREIGN KEY (`parentesco_id_parentesco`) REFERENCES `parentesco` (`id_parentesco`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_carga_familiar_usuario1` FOREIGN KEY (`usuario_id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `contacto_emergencia`
--
ALTER TABLE `contacto_emergencia`
  ADD CONSTRAINT `fk_contacto_emergencia_parentesco1` FOREIGN KEY (`parentesco_id_parentesco`) REFERENCES `parentesco` (`id_parentesco`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD CONSTRAINT `fk_departamento_area1` FOREIGN KEY (`area_id_area1`) REFERENCES `area` (`id_area`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `fk_usuario_cargo_trabajador` FOREIGN KEY (`cargo_trabajador_id_cargo_trabajador`) REFERENCES `cargo_trabajador` (`id_cargo_trabajador`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_usuario_departamento1` FOREIGN KEY (`departamento_id_departamentos`) REFERENCES `departamento` (`id_departamento`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_usuario_genero_trabajador1` FOREIGN KEY (`genero_trabajador_id_sexo_usuario`) REFERENCES `genero_trabajador` (`id_sexo_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `usuario_has_contacto_emergencia`
--
ALTER TABLE `usuario_has_contacto_emergencia`
  ADD CONSTRAINT `fk_usuario_has_contacto_emergencia_contacto_emergencia1` FOREIGN KEY (`contacto_emergencia_id_contacto_emergencia`) REFERENCES `contacto_emergencia` (`id_contacto_emergencia`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_usuario_has_contacto_emergencia_usuario1` FOREIGN KEY (`usuario_id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
