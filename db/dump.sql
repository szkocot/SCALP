--
-- PostgreSQL database dump
--
-- CREATE DATABASE bbd
--      WITH
--      OWNER = bbd
--      ENCODING = 'UTF8'
--      LC_COLLATE = 'Polish_Poland.1250'
--      LC_CTYPE = 'Polish_Poland.1250'
--      TABLESPACE = pg_default
--      CONNECTION LIMIT = -1;
-- Dumped from database version 10.6
-- Dumped by pg_dump version 10.6



SET session_replication_role = 'replica';

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
-- TOC entry 2948 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner:
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 196 (class 1259 OID 19211)
-- Name: acquisition; Type: TABLE; Schema: public; Owner: bbd
--

CREATE TABLE public.acquisition (
    id integer NOT NULL,
    image_type character varying(255),
    "pixelsX" character varying(255),
    "pixelsY" character varying(255)
);


ALTER TABLE public.acquisition OWNER TO bbd;

--
-- TOC entry 197 (class 1259 OID 19217)
-- Name: acquisition_id_seq; Type: SEQUENCE; Schema: public; Owner: bbd
--

CREATE SEQUENCE public.acquisition_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.acquisition_id_seq OWNER TO bbd;

--
-- TOC entry 2949 (class 0 OID 0)
-- Dependencies: 197
-- Name: acquisition_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.acquisition_id_seq OWNED BY public.acquisition.id;


--
-- TOC entry 198 (class 1259 OID 19219)
-- Name: app_version; Type: TABLE; Schema: public; Owner: bbd
--

CREATE TABLE public.app_version (
    id integer NOT NULL,
    ver real NOT NULL
);


ALTER TABLE public.app_version OWNER TO bbd;

--
-- TOC entry 199 (class 1259 OID 19222)
-- Name: app_version_id_seq; Type: SEQUENCE; Schema: public; Owner: bbd
--

CREATE SEQUENCE public.app_version_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_version_id_seq OWNER TO bbd;

--
-- TOC entry 2950 (class 0 OID 0)
-- Dependencies: 199
-- Name: app_version_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.app_version_id_seq OWNED BY public.app_version.id;


--
-- TOC entry 200 (class 1259 OID 19224)
-- Name: clinical; Type: TABLE; Schema: public; Owner: bbd
--

CREATE TABLE public.clinical (
    id integer NOT NULL,
    age_approx integer,
    anatom_site_general character varying(255),
    benign_malignant character varying(255),
    diagnosis character varying(255),
    diagnosis_confirm_type character varying(255),
    melanocytic character varying(255),
    sex character varying(255)
);


ALTER TABLE public.clinical OWNER TO bbd;

--
-- TOC entry 201 (class 1259 OID 19230)
-- Name: clinical_id_seq; Type: SEQUENCE; Schema: public; Owner: bbd
--

CREATE SEQUENCE public.clinical_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.clinical_id_seq OWNER TO bbd;

--
-- TOC entry 2951 (class 0 OID 0)
-- Dependencies: 201
-- Name: clinical_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.clinical_id_seq OWNED BY public.clinical.id;


--
-- TOC entry 202 (class 1259 OID 19232)
-- Name: creator; Type: TABLE; Schema: public; Owner: bbd
--

CREATE TABLE public.creator (
    id integer NOT NULL,
    _id character varying(255),
    name character varying(255)
);


ALTER TABLE public.creator OWNER TO bbd;

--
-- TOC entry 203 (class 1259 OID 19238)
-- Name: creator_id_seq; Type: SEQUENCE; Schema: public; Owner: bbd
--

CREATE SEQUENCE public.creator_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.creator_id_seq OWNER TO bbd;

--
-- TOC entry 2952 (class 0 OID 0)
-- Dependencies: 203
-- Name: creator_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.creator_id_seq OWNED BY public.creator.id;


--
-- TOC entry 204 (class 1259 OID 19240)
-- Name: dataset; Type: TABLE; Schema: public; Owner: bbd
--

CREATE TABLE public.dataset (
    id integer NOT NULL,
    _access_level integer,
    _id character varying(255),
    description character varying(255),
    license character varying(255),
    name character varying(255),
    updated character varying(255)
);


ALTER TABLE public.dataset OWNER TO bbd;

--
-- TOC entry 205 (class 1259 OID 19246)
-- Name: dataset_id_seq; Type: SEQUENCE; Schema: public; Owner: bbd
--

CREATE SEQUENCE public.dataset_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dataset_id_seq OWNER TO bbd;

--
-- TOC entry 2953 (class 0 OID 0)
-- Dependencies: 205
-- Name: dataset_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.dataset_id_seq OWNED BY public.dataset.id;


--
-- TOC entry 206 (class 1259 OID 19248)
-- Name: meta; Type: TABLE; Schema: public; Owner: bbd
--

CREATE TABLE public.meta (
    id integer NOT NULL,
    acquisition_id integer,
    clinical_id integer,
    unstructured_id integer
);


ALTER TABLE public.meta OWNER TO bbd;

--
-- TOC entry 207 (class 1259 OID 19251)
-- Name: meta_id_seq; Type: SEQUENCE; Schema: public; Owner: bbd
--

CREATE SEQUENCE public.meta_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.meta_id_seq OWNER TO bbd;

--
-- TOC entry 2954 (class 0 OID 0)
-- Dependencies: 207
-- Name: meta_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.meta_id_seq OWNED BY public.meta.id;


--
-- TOC entry 208 (class 1259 OID 19253)
-- Name: metadata; Type: TABLE; Schema: public; Owner: bbd
--

CREATE TABLE public.metadata (
    id integer NOT NULL,
    _model_type character varying(255),
    created timestamp(6) with time zone,
    dataset_id integer,
    name character varying(255),
    notes_id integer,
    updated timestamp(6) with time zone,
    _id character varying(255),
    creator_id integer,
    meta_id integer,
    image character varying(255),
    segmentation character varying(255)
);


ALTER TABLE public.metadata OWNER TO bbd;

--
-- TOC entry 209 (class 1259 OID 19259)
-- Name: metadata_id_seq; Type: SEQUENCE; Schema: public; Owner: bbd
--

CREATE SEQUENCE public.metadata_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.metadata_id_seq OWNER TO bbd;

--
-- TOC entry 2955 (class 0 OID 0)
-- Dependencies: 209
-- Name: metadata_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.metadata_id_seq OWNED BY public.metadata.id;


--
-- TOC entry 210 (class 1259 OID 19261)
-- Name: notes; Type: TABLE; Schema: public; Owner: bbd
--

CREATE TABLE public.notes (
    id integer NOT NULL,
    reviewed_id integer,
    tags character varying(255)
);


ALTER TABLE public.notes OWNER TO bbd;

--
-- TOC entry 211 (class 1259 OID 19264)
-- Name: notes_id_seq; Type: SEQUENCE; Schema: public; Owner: bbd
--

CREATE SEQUENCE public.notes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.notes_id_seq OWNER TO bbd;

--
-- TOC entry 2956 (class 0 OID 0)
-- Dependencies: 211
-- Name: notes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.notes_id_seq OWNED BY public.notes.id;


--
-- TOC entry 212 (class 1259 OID 19266)
-- Name: reviewed; Type: TABLE; Schema: public; Owner: bbd
--

CREATE TABLE public.reviewed (
    id integer NOT NULL,
    accepted boolean,
    "userId" character varying(255),
    "time" character varying(255)
);


ALTER TABLE public.reviewed OWNER TO bbd;

--
-- TOC entry 213 (class 1259 OID 19272)
-- Name: reviewed_id_seq; Type: SEQUENCE; Schema: public; Owner: bbd
--

CREATE SEQUENCE public.reviewed_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reviewed_id_seq OWNER TO bbd;

--
-- TOC entry 2957 (class 0 OID 0)
-- Dependencies: 213
-- Name: reviewed_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.reviewed_id_seq OWNED BY public.reviewed.id;


--
-- TOC entry 214 (class 1259 OID 19274)
-- Name: tag; Type: TABLE; Schema: public; Owner: bbd
--

CREATE TABLE public.tag (
    id integer NOT NULL,
    data character varying(255)
);


ALTER TABLE public.tag OWNER TO bbd;

--
-- TOC entry 215 (class 1259 OID 19277)
-- Name: tag_id_seq; Type: SEQUENCE; Schema: public; Owner: bbd
--

CREATE SEQUENCE public.tag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tag_id_seq OWNER TO bbd;

--
-- TOC entry 2958 (class 0 OID 0)
-- Dependencies: 215
-- Name: tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.tag_id_seq OWNED BY public.tag.id;


--
-- TOC entry 216 (class 1259 OID 19279)
-- Name: unstructured; Type: TABLE; Schema: public; Owner: bbd
--

CREATE TABLE public.unstructured (
    id integer NOT NULL,
    diagnosis character varying(255),
    id1 character varying(255),
    localization character varying(255),
    site character varying(255)
);


ALTER TABLE public.unstructured OWNER TO bbd;

--
-- TOC entry 217 (class 1259 OID 19285)
-- Name: unstructured_id_seq; Type: SEQUENCE; Schema: public; Owner: bbd
--

CREATE SEQUENCE public.unstructured_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.unstructured_id_seq OWNER TO bbd;

--
-- TOC entry 2959 (class 0 OID 0)
-- Dependencies: 217
-- Name: unstructured_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.unstructured_id_seq OWNED BY public.unstructured.id;


--
-- TOC entry 218 (class 1259 OID 19287)
-- Name: users; Type: TABLE; Schema: public; Owner: bbd
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(128),
    name character varying(128),
    surname character varying(128),
    email character varying(255),
    password text NOT NULL,
    admin boolean DEFAULT false,
    checked_images integer DEFAULT 0
);


ALTER TABLE public.users OWNER TO bbd;

--
-- TOC entry 219 (class 1259 OID 19295)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: bbd
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO bbd;

--
-- TOC entry 2960 (class 0 OID 0)
-- Dependencies: 219
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 2744 (class 2604 OID 19297)
-- Name: acquisition id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.acquisition ALTER COLUMN id SET DEFAULT nextval('public.acquisition_id_seq'::regclass);


--
-- TOC entry 2745 (class 2604 OID 19298)
-- Name: app_version id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.app_version ALTER COLUMN id SET DEFAULT nextval('public.app_version_id_seq'::regclass);


--
-- TOC entry 2746 (class 2604 OID 19299)
-- Name: clinical id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.clinical ALTER COLUMN id SET DEFAULT nextval('public.clinical_id_seq'::regclass);


--
-- TOC entry 2747 (class 2604 OID 19300)
-- Name: creator id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.creator ALTER COLUMN id SET DEFAULT nextval('public.creator_id_seq'::regclass);


--
-- TOC entry 2748 (class 2604 OID 19301)
-- Name: dataset id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.dataset ALTER COLUMN id SET DEFAULT nextval('public.dataset_id_seq'::regclass);


--
-- TOC entry 2749 (class 2604 OID 19302)
-- Name: meta id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.meta ALTER COLUMN id SET DEFAULT nextval('public.meta_id_seq'::regclass);


--
-- TOC entry 2750 (class 2604 OID 19303)
-- Name: metadata id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.metadata ALTER COLUMN id SET DEFAULT nextval('public.metadata_id_seq'::regclass);


--
-- TOC entry 2751 (class 2604 OID 19304)
-- Name: notes id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.notes ALTER COLUMN id SET DEFAULT nextval('public.notes_id_seq'::regclass);


--
-- TOC entry 2752 (class 2604 OID 19305)
-- Name: reviewed id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.reviewed ALTER COLUMN id SET DEFAULT nextval('public.reviewed_id_seq'::regclass);


--
-- TOC entry 2753 (class 2604 OID 19306)
-- Name: tag id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.tag ALTER COLUMN id SET DEFAULT nextval('public.tag_id_seq'::regclass);


--
-- TOC entry 2754 (class 2604 OID 19307)
-- Name: unstructured id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.unstructured ALTER COLUMN id SET DEFAULT nextval('public.unstructured_id_seq'::regclass);


--
-- TOC entry 2757 (class 2604 OID 19308)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);






ALTER TABLE ONLY public.acquisition
    ADD CONSTRAINT acquisition_pkey PRIMARY KEY (id);


--
-- TOC entry 2761 (class 2606 OID 19312)
-- Name: app_version app_version_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.app_version
    ADD CONSTRAINT app_version_pkey PRIMARY KEY (id);


--
-- TOC entry 2763 (class 2606 OID 19314)
-- Name: clinical clinical_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.clinical
    ADD CONSTRAINT clinical_pkey PRIMARY KEY (id);


--
-- TOC entry 2765 (class 2606 OID 19316)
-- Name: creator creator_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.creator
    ADD CONSTRAINT creator_pkey PRIMARY KEY (id);


--
-- TOC entry 2767 (class 2606 OID 19318)
-- Name: dataset dataset_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.dataset
    ADD CONSTRAINT dataset_pkey PRIMARY KEY (id);


--
-- TOC entry 2771 (class 2606 OID 19320)
-- Name: meta meta_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.meta
    ADD CONSTRAINT meta_pkey PRIMARY KEY (id);


--
-- TOC entry 2777 (class 2606 OID 19322)
-- Name: metadata metadata_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.metadata
    ADD CONSTRAINT metadata_pkey PRIMARY KEY (id);


--
-- TOC entry 2779 (class 2606 OID 19324)
-- Name: notes notes_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.notes
    ADD CONSTRAINT notes_pkey PRIMARY KEY (id);


--
-- TOC entry 2781 (class 2606 OID 19326)
-- Name: reviewed reviewed_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.reviewed
    ADD CONSTRAINT reviewed_pkey PRIMARY KEY (id);


--
-- TOC entry 2783 (class 2606 OID 19328)
-- Name: tag tag_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.tag
    ADD CONSTRAINT tag_pkey PRIMARY KEY (id);


--
-- TOC entry 2785 (class 2606 OID 19330)
-- Name: unstructured unstructured_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.unstructured
    ADD CONSTRAINT unstructured_pkey PRIMARY KEY (id);


--
-- TOC entry 2787 (class 2606 OID 19332)
-- Name: users username_unique; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT username_unique UNIQUE (username);


--
-- TOC entry 2789 (class 2606 OID 19334)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 2768 (class 1259 OID 19335)
-- Name: fki_FK_acquisition; Type: INDEX; Schema: public; Owner: bbd
--

CREATE INDEX "fki_FK_acquisition" ON public.meta USING btree (acquisition_id);


--
-- TOC entry 2769 (class 1259 OID 19336)
-- Name: fki_FK_clinical; Type: INDEX; Schema: public; Owner: bbd
--

CREATE INDEX "fki_FK_clinical" ON public.meta USING btree (clinical_id);


--
-- TOC entry 2772 (class 1259 OID 19337)
-- Name: fki_FK_creator; Type: INDEX; Schema: public; Owner: bbd
--

CREATE INDEX "fki_FK_creator" ON public.metadata USING btree (creator_id);


--
-- TOC entry 2773 (class 1259 OID 19338)
-- Name: fki_FK_dataset; Type: INDEX; Schema: public; Owner: bbd
--

CREATE INDEX "fki_FK_dataset" ON public.metadata USING btree (dataset_id);


--
-- TOC entry 2774 (class 1259 OID 19339)
-- Name: fki_FK_meta; Type: INDEX; Schema: public; Owner: bbd
--

CREATE INDEX "fki_FK_meta" ON public.metadata USING btree (meta_id);


--
-- TOC entry 2775 (class 1259 OID 19340)
-- Name: fki_FK_notes; Type: INDEX; Schema: public; Owner: bbd
--

CREATE INDEX "fki_FK_notes" ON public.metadata USING btree (notes_id);


--
-- TOC entry 2790 (class 2606 OID 19341)
-- Name: meta FK_acquisition; Type: FK CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.meta
    ADD CONSTRAINT "FK_acquisition" FOREIGN KEY (acquisition_id) REFERENCES public.acquisition(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2791 (class 2606 OID 19346)
-- Name: meta FK_clinical; Type: FK CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.meta
    ADD CONSTRAINT "FK_clinical" FOREIGN KEY (clinical_id) REFERENCES public.clinical(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2793 (class 2606 OID 19351)
-- Name: metadata FK_creator; Type: FK CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.metadata
    ADD CONSTRAINT "FK_creator" FOREIGN KEY (creator_id) REFERENCES public.creator(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2794 (class 2606 OID 19356)
-- Name: metadata FK_dataset; Type: FK CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.metadata
    ADD CONSTRAINT "FK_dataset" FOREIGN KEY (dataset_id) REFERENCES public.dataset(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2795 (class 2606 OID 19361)
-- Name: metadata FK_meta; Type: FK CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.metadata
    ADD CONSTRAINT "FK_meta" FOREIGN KEY (meta_id) REFERENCES public.meta(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2792 (class 2606 OID 19366)
-- Name: meta FK_unstructured; Type: FK CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.meta
    ADD CONSTRAINT "FK_unstructured" FOREIGN KEY (id) REFERENCES public.unstructured(id) ON UPDATE CASCADE ON DELETE CASCADE;


-- Completed on 2019-02-09 20:22:13

--
-- PostgreSQL database dump complete
--

SET session_replication_role = 'origin';