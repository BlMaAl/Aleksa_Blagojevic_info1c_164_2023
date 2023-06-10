-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:3306
-- Généré le : sam. 10 juin 2023 à 13:36
-- Version du serveur : 5.7.24
-- Version de PHP : 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `aleksa_blagojevic_martins_info1c_mpd`
--

-- --------------------------------------------------------

--
-- Structure de la table `t_categorie`
--

CREATE TABLE `t_categorie` (
  `id_categorie` int(11) NOT NULL,
  `nom_categorie` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `t_question_reponse`
--

CREATE TABLE `t_question_reponse` (
  `id_question_reponse` int(11) NOT NULL,
  `question` text NOT NULL,
  `question_image` varchar(50) NOT NULL,
  `reponse` text NOT NULL,
  `reponse_image` varchar(50) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `t_questreponse_avoir_categorie`
--

CREATE TABLE `t_questreponse_avoir_categorie` (
  `id_questreponse_avoir_categorie` int(11) NOT NULL,
  `fk_question_reponse` int(11) NOT NULL,
  `fk_categorie` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `t_utilisateurs`
--

CREATE TABLE `t_utilisateurs` (
  `id_utilisateur` int(11) NOT NULL,
  `nom_utilisateur` varchar(50) NOT NULL,
  `prenom_utilisateur` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `t_utilisateurs_creer_question_reponses`
--

CREATE TABLE `t_utilisateurs_creer_question_reponses` (
  `id_utilisateurs_creer_question_reponses` int(11) NOT NULL,
  `fk_utilisateur` int(11) NOT NULL,
  `fk_question_reponse` int(11) NOT NULL,
  `date_creation_qr` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `t_categorie`
--
ALTER TABLE `t_categorie`
  ADD PRIMARY KEY (`id_categorie`);

--
-- Index pour la table `t_question_reponse`
--
ALTER TABLE `t_question_reponse`
  ADD PRIMARY KEY (`id_question_reponse`);

--
-- Index pour la table `t_questreponse_avoir_categorie`
--
ALTER TABLE `t_questreponse_avoir_categorie`
  ADD PRIMARY KEY (`id_questreponse_avoir_categorie`),
  ADD KEY `fk_question_reponse` (`fk_question_reponse`),
  ADD KEY `fk_categorie` (`fk_categorie`);

--
-- Index pour la table `t_utilisateurs`
--
ALTER TABLE `t_utilisateurs`
  ADD PRIMARY KEY (`id_utilisateur`);

--
-- Index pour la table `t_utilisateurs_creer_question_reponses`
--
ALTER TABLE `t_utilisateurs_creer_question_reponses`
  ADD PRIMARY KEY (`id_utilisateurs_creer_question_reponses`),
  ADD KEY `fk_utilisateur` (`fk_utilisateur`),
  ADD KEY `fk_question_reponse` (`fk_question_reponse`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `t_categorie`
--
ALTER TABLE `t_categorie`
  MODIFY `id_categorie` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_question_reponse`
--
ALTER TABLE `t_question_reponse`
  MODIFY `id_question_reponse` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_questreponse_avoir_categorie`
--
ALTER TABLE `t_questreponse_avoir_categorie`
  MODIFY `id_questreponse_avoir_categorie` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_utilisateurs`
--
ALTER TABLE `t_utilisateurs`
  MODIFY `id_utilisateur` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_utilisateurs_creer_question_reponses`
--
ALTER TABLE `t_utilisateurs_creer_question_reponses`
  MODIFY `id_utilisateurs_creer_question_reponses` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `t_questreponse_avoir_categorie`
--
ALTER TABLE `t_questreponse_avoir_categorie`
  ADD CONSTRAINT `t_questreponse_avoir_categorie_ibfk_1` FOREIGN KEY (`fk_question_reponse`) REFERENCES `t_question_reponse` (`id_question_reponse`),
  ADD CONSTRAINT `t_questreponse_avoir_categorie_ibfk_2` FOREIGN KEY (`fk_categorie`) REFERENCES `t_categorie` (`id_categorie`);

--
-- Contraintes pour la table `t_utilisateurs_creer_question_reponses`
--
ALTER TABLE `t_utilisateurs_creer_question_reponses`
  ADD CONSTRAINT `t_utilisateurs_creer_question_reponses_ibfk_1` FOREIGN KEY (`fk_utilisateur`) REFERENCES `t_utilisateurs` (`id_utilisateur`),
  ADD CONSTRAINT `t_utilisateurs_creer_question_reponses_ibfk_2` FOREIGN KEY (`fk_question_reponse`) REFERENCES `t_question_reponse` (`id_question_reponse`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
