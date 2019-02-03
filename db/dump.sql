-- -- -- Database: bbd
-- --
-- -- -- DROP DATABASE bbd;

--  CREATE DATABASE bbd
--      WITH
--      OWNER = bbd
--      ENCODING = 'UTF8'
--      LC_COLLATE = 'Polish_Poland.1250'
--      LC_CTYPE = 'Polish_Poland.1250'
--      TABLESPACE = pg_default
--      CONNECTION LIMIT = -1;

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';

SET default_tablespace = '';

SET default_with_oids = false;

CREATE TABLE public.acquisition (
    id SERIAL PRIMARY KEY,
    image_type character varying(255),
    "pixelsX" character varying(255),
    "pixelsY" character varying(255)
);

ALTER TABLE public.acquisition OWNER TO bbd;

CREATE TABLE public.clinical (
    id SERIAL PRIMARY KEY,
    age_approx integer,
    anatom_site_general character varying(255),
    benign_malignant character varying(255),
    diagnosis character varying(255),
    diagnosis_confirm_type character varying(255),
    melanocytic character varying(255),
    sex character varying(255)
);

ALTER TABLE public.clinical OWNER TO bbd;

CREATE TABLE public.creator (
    id SERIAL PRIMARY KEY,
    _id character varying(255),
    name character varying(255)
);

ALTER TABLE public.creator OWNER TO bbd;

CREATE TABLE public.dataset (
    id SERIAL PRIMARY KEY,
    _access_level integer,
    _id character varying(255),
    description character varying(255),
    license character varying(255),
    name character varying(255),
    updated character varying(255)
);

ALTER TABLE public.dataset OWNER TO bbd;

CREATE TABLE public.meta (
    id SERIAL PRIMARY KEY,
    acquisition_id integer,
    clinical_id integer,
    unstructured_id integer
);

ALTER TABLE public.meta OWNER TO bbd;

CREATE TABLE public.metadata (
    id SERIAL PRIMARY KEY,
    _model_type character varying(255),
    created timestamp(6) with time zone,
    dataset_id integer,
    name character varying(255),
    notes_id integer,
    updated timestamp(6) with time zone,
    _id character varying(255),
    creator_id integer,
    meta_id integer
);


ALTER TABLE public.metadata OWNER TO bbd;

CREATE TABLE public.notes (
    id SERIAL PRIMARY KEY,
    reviewed_id integer,
    tags character varying(255)
);

ALTER TABLE public.notes OWNER TO bbd;

CREATE TABLE public.tag (
    id SERIAL PRIMARY KEY,
    data character varying(255)
);

ALTER TABLE public.tag OWNER TO bbd;

CREATE TABLE public.unstructured (
    id SERIAL PRIMARY KEY,
    diagnosis character varying(255),
    id1 character varying(255),
    localization character varying(255),
    site character varying(255)
);

ALTER TABLE public.unstructured OWNER TO bbd;

CREATE TABLE public.users (
    id SERIAL PRIMARY KEY,
    username character varying(128),
    name character varying(128),
    surname character varying(128),
    email character varying(255),
    password text NOT NULL,
    admin boolean DEFAULT False
);

ALTER TABLE public.users OWNER TO bbd;

CREATE TABLE public.app_version (
    id SERIAL PRIMARY KEY,
    app_version real NOT NULL
);

CREATE TABLE public.reviewed
(
    id SERIAL PRIMARY KEY,
    accepted boolean,
    "userId" character varying(255),
    "time" character varying(255)
)
WITH (
    OIDS = FALSE
);

ALTER TABLE public.reviewed OWNER to bbd;

ALTER TABLE public.app_version OWNER TO bbd;

CREATE INDEX "fki_FK_acquisition" ON public.meta USING btree (acquisition_id);

CREATE INDEX "fki_FK_clinical" ON public.meta USING btree (clinical_id);

CREATE INDEX "fki_FK_creator" ON public.metadata USING btree (creator_id);

CREATE INDEX "fki_FK_dataset" ON public.metadata USING btree (dataset_id);

CREATE INDEX "fki_FK_meta" ON public.metadata USING btree (meta_id);

CREATE INDEX "fki_FK_notes" ON public.metadata USING btree (notes_id);

ALTER TABLE ONLY public.meta ADD CONSTRAINT "FK_acquisition" FOREIGN KEY (acquisition_id) REFERENCES public.acquisition(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY public.meta ADD CONSTRAINT "FK_clinical" FOREIGN KEY (clinical_id) REFERENCES public.clinical(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY public.metadata ADD CONSTRAINT "FK_creator" FOREIGN KEY (creator_id) REFERENCES public.creator(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY public.metadata ADD CONSTRAINT "FK_dataset" FOREIGN KEY (dataset_id) REFERENCES public.dataset(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY public.metadata ADD CONSTRAINT "FK_meta" FOREIGN KEY (meta_id) REFERENCES public.meta(id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY public.meta ADD CONSTRAINT "FK_unstructured" FOREIGN KEY (id) REFERENCES public.unstructured(id) ON UPDATE CASCADE ON DELETE CASCADE;
