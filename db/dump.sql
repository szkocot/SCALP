--
-- PostgreSQL database dump
--

-- Dumped from database version 10.5
-- Dumped by pg_dump version 10.5

-- Started on 2018-10-23 23:17:51

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 12924)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2885 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 201 (class 1259 OID 16444)
-- Name: acquisition; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.acquisition (
    id integer NOT NULL,
    image_type character varying(256),
    "pixelsX" character varying(256),
    "pixelsY" character varying(256)
);


ALTER TABLE public.acquisition OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 16473)
-- Name: clinical; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clinical (
    id integer NOT NULL,
    age_approx integer,
    anatom_site_general character varying(256),
    benign_malignant character varying(256),
    diagnosis character varying(256),
    diagnosis_confirm_type character varying(256),
    melanocytic character varying(256),
    sex character varying(256)
);


ALTER TABLE public.clinical OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 16500)
-- Name: creator; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.creator (
    id integer NOT NULL,
    _id character varying(256),
    name character varying(256)
);


ALTER TABLE public.creator OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16492)
-- Name: dataset; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.dataset (
    id integer NOT NULL,
    _access_level integer,
    _id character varying(256),
    description character varying(256),
    license character varying(256),
    name character varying(256),
    updated character varying(256)
);


ALTER TABLE public.dataset OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16452)
-- Name: meta; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.meta (
    id integer NOT NULL,
    acquisition_id integer,
    clinical_id integer,
    unstructured_id integer
);


ALTER TABLE public.meta OWNER TO postgres;

--
-- TOC entry 197 (class 1259 OID 16403)
-- Name: metadata; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.metadata (
    id integer NOT NULL,
    _model_type character varying(256),
    created timestamp(6) with time zone,
    dataset_id integer,
    name character varying(256),
    notes_id integer,
    updated timestamp(6) with time zone,
    _id character varying(256),
    creator_id integer,
    meta_id integer
);


ALTER TABLE public.metadata OWNER TO postgres;

--
-- TOC entry 198 (class 1259 OID 16411)
-- Name: notes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.notes (
    id integer NOT NULL,
    tags_id integer NOT NULL,
    accepted boolean,
    "time" timestamp(6) with time zone,
    user_id character varying(256)
);


ALTER TABLE public.notes OWNER TO postgres;

--
-- TOC entry 199 (class 1259 OID 16416)
-- Name: tags; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tags (
    id integer NOT NULL,
    data json
);


ALTER TABLE public.tags OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 16430)
-- Name: unstructured; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.unstructured (
    id integer NOT NULL,
    diagnosis character varying(256),
    id1 character varying(256),
    localization character varying(256),
    site character varying(256)
);


ALTER TABLE public.unstructured OWNER TO postgres;

--
-- TOC entry 196 (class 1259 OID 16395)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id bigint NOT NULL,
    username character varying(128),
    name character varying(128),
    surnname character varying(128),
    email character varying(256)
);


ALTER TABLE public.users OWNER TO postgres;
ALTER TABLE ONLY public.clinical
    ADD CONSTRAINT "PK_clinical" PRIMARY KEY (id);


--
-- TOC entry 2713 (class 2606 OID 16399)
-- Name: users User_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT "User_pkey" PRIMARY KEY (id);


--
-- TOC entry 2738 (class 2606 OID 16507)
-- Name: creator creator_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.creator
    ADD CONSTRAINT creator_pkey PRIMARY KEY (id);


--
-- TOC entry 2736 (class 2606 OID 16499)
-- Name: dataset dataset_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.dataset
    ADD CONSTRAINT dataset_pkey PRIMARY KEY (id);


--
-- TOC entry 2728 (class 2606 OID 16451)
-- Name: acquisition meta_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acquisition
    ADD CONSTRAINT meta_pkey PRIMARY KEY (id);


--
-- TOC entry 2732 (class 2606 OID 16456)
-- Name: meta meta_pkey1; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meta
    ADD CONSTRAINT meta_pkey1 PRIMARY KEY (id);


--
-- TOC entry 2719 (class 2606 OID 16410)
-- Name: metadata metadata_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.metadata
    ADD CONSTRAINT metadata_pkey PRIMARY KEY (id);


--
-- TOC entry 2722 (class 2606 OID 16415)
-- Name: notes notes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notes
    ADD CONSTRAINT notes_pkey PRIMARY KEY (id);


--
-- TOC entry 2724 (class 2606 OID 16423)
-- Name: tags tags_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_pkey PRIMARY KEY (id);


--
-- TOC entry 2726 (class 2606 OID 16437)
-- Name: unstructured unstructured_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.unstructured
    ADD CONSTRAINT unstructured_pkey PRIMARY KEY (id);


--
-- TOC entry 2729 (class 1259 OID 16462)
-- Name: fki_FK_acquisition; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "fki_FK_acquisition" ON public.meta USING btree (acquisition_id);


--
-- TOC entry 2730 (class 1259 OID 16486)
-- Name: fki_FK_clinical; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "fki_FK_clinical" ON public.meta USING btree (clinical_id);


--
-- TOC entry 2714 (class 1259 OID 16513)
-- Name: fki_FK_creator; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "fki_FK_creator" ON public.metadata USING btree (creator_id);


--
-- TOC entry 2715 (class 1259 OID 16519)
-- Name: fki_FK_dataset; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "fki_FK_dataset" ON public.metadata USING btree (dataset_id);


--
-- TOC entry 2716 (class 1259 OID 16525)
-- Name: fki_FK_meta; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "fki_FK_meta" ON public.metadata USING btree (meta_id);


--
-- TOC entry 2717 (class 1259 OID 16531)
-- Name: fki_FK_notes; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "fki_FK_notes" ON public.metadata USING btree (notes_id);


--
-- TOC entry 2720 (class 1259 OID 16429)
-- Name: fki_FK_tags_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "fki_FK_tags_id" ON public.notes USING btree (tags_id);


--
-- TOC entry 2744 (class 2606 OID 16463)
-- Name: meta FK_acquisition; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meta
    ADD CONSTRAINT "FK_acquisition" FOREIGN KEY (acquisition_id) REFERENCES public.acquisition(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2745 (class 2606 OID 16481)
-- Name: meta FK_clinical; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meta
    ADD CONSTRAINT "FK_clinical" FOREIGN KEY (clinical_id) REFERENCES public.clinical(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2739 (class 2606 OID 16508)
-- Name: metadata FK_creator; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.metadata
    ADD CONSTRAINT "FK_creator" FOREIGN KEY (creator_id) REFERENCES public.creator(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2740 (class 2606 OID 16514)
-- Name: metadata FK_dataset; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.metadata
    ADD CONSTRAINT "FK_dataset" FOREIGN KEY (dataset_id) REFERENCES public.dataset(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2741 (class 2606 OID 16520)
-- Name: metadata FK_meta; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.metadata
    ADD CONSTRAINT "FK_meta" FOREIGN KEY (meta_id) REFERENCES public.meta(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2742 (class 2606 OID 16526)
-- Name: metadata FK_notes; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.metadata
    ADD CONSTRAINT "FK_notes" FOREIGN KEY (notes_id) REFERENCES public.notes(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2743 (class 2606 OID 16468)
-- Name: notes FK_tags; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notes
    ADD CONSTRAINT "FK_tags" FOREIGN KEY (tags_id) REFERENCES public.tags(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2746 (class 2606 OID 16487)
-- Name: meta FK_unstructured; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.meta
    ADD CONSTRAINT "FK_unstructured" FOREIGN KEY (id) REFERENCES public.unstructured(id) ON UPDATE CASCADE ON DELETE CASCADE;


-- Completed on 2018-10-23 23:17:52

--
-- PostgreSQL database dump complete
--

