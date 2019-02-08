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

-- Started on 2019-02-06 18:55:02

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
-- TOC entry 2947 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 197 (class 1259 OID 17227)
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
-- TOC entry 196 (class 1259 OID 17225)
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
-- TOC entry 2948 (class 0 OID 0)
-- Dependencies: 196
-- Name: acquisition_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.acquisition_id_seq OWNED BY public.acquisition.id;


--
-- TOC entry 217 (class 1259 OID 17329)
-- Name: app_version; Type: TABLE; Schema: public; Owner: bbd
--

CREATE TABLE public.app_version (
    id integer NOT NULL,
    app_version real NOT NULL
);


ALTER TABLE public.app_version OWNER TO bbd;

--
-- TOC entry 216 (class 1259 OID 17327)
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
-- TOC entry 2949 (class 0 OID 0)
-- Dependencies: 216
-- Name: app_version_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.app_version_id_seq OWNED BY public.app_version.id;


--
-- TOC entry 199 (class 1259 OID 17238)
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
-- TOC entry 198 (class 1259 OID 17236)
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
-- TOC entry 2950 (class 0 OID 0)
-- Dependencies: 198
-- Name: clinical_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.clinical_id_seq OWNED BY public.clinical.id;


--
-- TOC entry 201 (class 1259 OID 17249)
-- Name: creator; Type: TABLE; Schema: public; Owner: bbd
--

CREATE TABLE public.creator (
    id integer NOT NULL,
    _id character varying(255),
    name character varying(255)
);


ALTER TABLE public.creator OWNER TO bbd;

--
-- TOC entry 200 (class 1259 OID 17247)
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
-- TOC entry 2951 (class 0 OID 0)
-- Dependencies: 200
-- Name: creator_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.creator_id_seq OWNED BY public.creator.id;


--
-- TOC entry 203 (class 1259 OID 17260)
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
-- TOC entry 202 (class 1259 OID 17258)
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
-- TOC entry 2952 (class 0 OID 0)
-- Dependencies: 202
-- Name: dataset_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.dataset_id_seq OWNED BY public.dataset.id;


--
-- TOC entry 205 (class 1259 OID 17271)
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
-- TOC entry 204 (class 1259 OID 17269)
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
-- TOC entry 2953 (class 0 OID 0)
-- Dependencies: 204
-- Name: meta_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.meta_id_seq OWNED BY public.meta.id;


--
-- TOC entry 207 (class 1259 OID 17279)
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
-- TOC entry 206 (class 1259 OID 17277)
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
-- TOC entry 2954 (class 0 OID 0)
-- Dependencies: 206
-- Name: metadata_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.metadata_id_seq OWNED BY public.metadata.id;


--
-- TOC entry 209 (class 1259 OID 17290)
-- Name: notes; Type: TABLE; Schema: public; Owner: bbd
--

CREATE TABLE public.notes (
    id integer NOT NULL,
    reviewed_id integer,
    tags character varying(255)
);


ALTER TABLE public.notes OWNER TO bbd;

--
-- TOC entry 208 (class 1259 OID 17288)
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
-- TOC entry 2955 (class 0 OID 0)
-- Dependencies: 208
-- Name: notes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.notes_id_seq OWNED BY public.notes.id;


--
-- TOC entry 219 (class 1259 OID 17337)
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
-- TOC entry 218 (class 1259 OID 17335)
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
-- TOC entry 2956 (class 0 OID 0)
-- Dependencies: 218
-- Name: reviewed_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.reviewed_id_seq OWNED BY public.reviewed.id;


--
-- TOC entry 211 (class 1259 OID 17298)
-- Name: tag; Type: TABLE; Schema: public; Owner: bbd
--

CREATE TABLE public.tag (
    id integer NOT NULL,
    data character varying(255)
);


ALTER TABLE public.tag OWNER TO bbd;

--
-- TOC entry 210 (class 1259 OID 17296)
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
-- TOC entry 2957 (class 0 OID 0)
-- Dependencies: 210
-- Name: tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.tag_id_seq OWNED BY public.tag.id;


--
-- TOC entry 213 (class 1259 OID 17306)
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
-- TOC entry 212 (class 1259 OID 17304)
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
-- TOC entry 2958 (class 0 OID 0)
-- Dependencies: 212
-- Name: unstructured_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.unstructured_id_seq OWNED BY public.unstructured.id;


--
-- TOC entry 215 (class 1259 OID 17317)
-- Name: users; Type: TABLE; Schema: public; Owner: bbd
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(128),
    name character varying(128),
    surname character varying(128),
    email character varying(255),
    password text NOT NULL,
    admin boolean DEFAULT false
);


ALTER TABLE public.users OWNER TO bbd;

--
-- TOC entry 214 (class 1259 OID 17315)
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
-- TOC entry 2959 (class 0 OID 0)
-- Dependencies: 214
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: bbd
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 2744 (class 2604 OID 17230)
-- Name: acquisition id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.acquisition ALTER COLUMN id SET DEFAULT nextval('public.acquisition_id_seq'::regclass);


--
-- TOC entry 2755 (class 2604 OID 17332)
-- Name: app_version id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.app_version ALTER COLUMN id SET DEFAULT nextval('public.app_version_id_seq'::regclass);


--
-- TOC entry 2745 (class 2604 OID 17241)
-- Name: clinical id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.clinical ALTER COLUMN id SET DEFAULT nextval('public.clinical_id_seq'::regclass);


--
-- TOC entry 2746 (class 2604 OID 17252)
-- Name: creator id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.creator ALTER COLUMN id SET DEFAULT nextval('public.creator_id_seq'::regclass);


--
-- TOC entry 2747 (class 2604 OID 17263)
-- Name: dataset id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.dataset ALTER COLUMN id SET DEFAULT nextval('public.dataset_id_seq'::regclass);


--
-- TOC entry 2748 (class 2604 OID 17274)
-- Name: meta id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.meta ALTER COLUMN id SET DEFAULT nextval('public.meta_id_seq'::regclass);


--
-- TOC entry 2749 (class 2604 OID 17282)
-- Name: metadata id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.metadata ALTER COLUMN id SET DEFAULT nextval('public.metadata_id_seq'::regclass);


--
-- TOC entry 2750 (class 2604 OID 17293)
-- Name: notes id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.notes ALTER COLUMN id SET DEFAULT nextval('public.notes_id_seq'::regclass);


--
-- TOC entry 2756 (class 2604 OID 17340)
-- Name: reviewed id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.reviewed ALTER COLUMN id SET DEFAULT nextval('public.reviewed_id_seq'::regclass);


--
-- TOC entry 2751 (class 2604 OID 17301)
-- Name: tag id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.tag ALTER COLUMN id SET DEFAULT nextval('public.tag_id_seq'::regclass);


--
-- TOC entry 2752 (class 2604 OID 17309)
-- Name: unstructured id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.unstructured ALTER COLUMN id SET DEFAULT nextval('public.unstructured_id_seq'::regclass);


--
-- TOC entry 2753 (class 2604 OID 17320)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


ALTER TABLE ONLY public.acquisition
    ADD CONSTRAINT acquisition_pkey PRIMARY KEY (id);


--
-- TOC entry 2786 (class 2606 OID 17334)
-- Name: app_version app_version_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.app_version
    ADD CONSTRAINT app_version_pkey PRIMARY KEY (id);


--
-- TOC entry 2760 (class 2606 OID 17246)
-- Name: clinical clinical_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.clinical
    ADD CONSTRAINT clinical_pkey PRIMARY KEY (id);


--
-- TOC entry 2762 (class 2606 OID 17257)
-- Name: creator creator_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.creator
    ADD CONSTRAINT creator_pkey PRIMARY KEY (id);


--
-- TOC entry 2764 (class 2606 OID 17268)
-- Name: dataset dataset_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.dataset
    ADD CONSTRAINT dataset_pkey PRIMARY KEY (id);


--
-- TOC entry 2768 (class 2606 OID 17276)
-- Name: meta meta_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.meta
    ADD CONSTRAINT meta_pkey PRIMARY KEY (id);


--
-- TOC entry 2774 (class 2606 OID 17287)
-- Name: metadata metadata_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.metadata
    ADD CONSTRAINT metadata_pkey PRIMARY KEY (id);


--
-- TOC entry 2776 (class 2606 OID 17295)
-- Name: notes notes_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.notes
    ADD CONSTRAINT notes_pkey PRIMARY KEY (id);


--
-- TOC entry 2788 (class 2606 OID 17345)
-- Name: reviewed reviewed_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.reviewed
    ADD CONSTRAINT reviewed_pkey PRIMARY KEY (id);


--
-- TOC entry 2778 (class 2606 OID 17303)
-- Name: tag tag_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.tag
    ADD CONSTRAINT tag_pkey PRIMARY KEY (id);


--
-- TOC entry 2780 (class 2606 OID 17314)
-- Name: unstructured unstructured_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.unstructured
    ADD CONSTRAINT unstructured_pkey PRIMARY KEY (id);


--
-- TOC entry 2782 (class 2606 OID 17391)
-- Name: users username_unique; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT username_unique UNIQUE (username);


--
-- TOC entry 2784 (class 2606 OID 17326)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 2765 (class 1259 OID 17346)
-- Name: fki_FK_acquisition; Type: INDEX; Schema: public; Owner: bbd
--

CREATE INDEX "fki_FK_acquisition" ON public.meta USING btree (acquisition_id);


--
-- TOC entry 2766 (class 1259 OID 17347)
-- Name: fki_FK_clinical; Type: INDEX; Schema: public; Owner: bbd
--

CREATE INDEX "fki_FK_clinical" ON public.meta USING btree (clinical_id);


--
-- TOC entry 2769 (class 1259 OID 17348)
-- Name: fki_FK_creator; Type: INDEX; Schema: public; Owner: bbd
--

CREATE INDEX "fki_FK_creator" ON public.metadata USING btree (creator_id);


--
-- TOC entry 2770 (class 1259 OID 17349)
-- Name: fki_FK_dataset; Type: INDEX; Schema: public; Owner: bbd
--

CREATE INDEX "fki_FK_dataset" ON public.metadata USING btree (dataset_id);


--
-- TOC entry 2771 (class 1259 OID 17350)
-- Name: fki_FK_meta; Type: INDEX; Schema: public; Owner: bbd
--

CREATE INDEX "fki_FK_meta" ON public.metadata USING btree (meta_id);


--
-- TOC entry 2772 (class 1259 OID 17351)
-- Name: fki_FK_notes; Type: INDEX; Schema: public; Owner: bbd
--

CREATE INDEX "fki_FK_notes" ON public.metadata USING btree (notes_id);


--
-- TOC entry 2789 (class 2606 OID 17352)
-- Name: meta FK_acquisition; Type: FK CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.meta
    ADD CONSTRAINT "FK_acquisition" FOREIGN KEY (acquisition_id) REFERENCES public.acquisition(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2790 (class 2606 OID 17357)
-- Name: meta FK_clinical; Type: FK CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.meta
    ADD CONSTRAINT "FK_clinical" FOREIGN KEY (clinical_id) REFERENCES public.clinical(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2792 (class 2606 OID 17362)
-- Name: metadata FK_creator; Type: FK CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.metadata
    ADD CONSTRAINT "FK_creator" FOREIGN KEY (creator_id) REFERENCES public.creator(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2793 (class 2606 OID 17367)
-- Name: metadata FK_dataset; Type: FK CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.metadata
    ADD CONSTRAINT "FK_dataset" FOREIGN KEY (dataset_id) REFERENCES public.dataset(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2794 (class 2606 OID 17372)
-- Name: metadata FK_meta; Type: FK CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.metadata
    ADD CONSTRAINT "FK_meta" FOREIGN KEY (meta_id) REFERENCES public.meta(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2791 (class 2606 OID 17377)
-- Name: meta FK_unstructured; Type: FK CONSTRAINT; Schema: public; Owner: bbd
--

ALTER TABLE ONLY public.meta
    ADD CONSTRAINT "FK_unstructured" FOREIGN KEY (id) REFERENCES public.unstructured(id) ON UPDATE CASCADE ON DELETE CASCADE;


-- Completed on 2019-02-06 18:55:03

--
-- PostgreSQL database dump complete
--

