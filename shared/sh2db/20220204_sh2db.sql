--
-- PostgreSQL database dump
--

-- Dumped from database version 10.19 (Ubuntu 10.19-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.19 (Ubuntu 10.19-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO "SH2";

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO "SH2";

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO "SH2";

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO "SH2";

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO "SH2";

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO "SH2";

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO "SH2";

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO "SH2";

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO "SH2";

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO "SH2";

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO "SH2";

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO "SH2";

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: chain; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.chain (
    id bigint NOT NULL,
    "chain_ID" character varying(1) NOT NULL,
    structure_id bigint NOT NULL
);


ALTER TABLE public.chain OWNER TO "SH2";

--
-- Name: chain_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.chain_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.chain_id_seq OWNER TO "SH2";

--
-- Name: chain_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.chain_id_seq OWNED BY public.chain.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO "SH2";

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO "SH2";

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO "SH2";

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO "SH2";

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO "SH2";

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO "SH2";

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO "SH2";

--
-- Name: pdbdata; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.pdbdata (
    id bigint NOT NULL,
    pdb text NOT NULL
);


ALTER TABLE public.pdbdata OWNER TO "SH2";

--
-- Name: pdbdata_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.pdbdata_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pdbdata_id_seq OWNER TO "SH2";

--
-- Name: pdbdata_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.pdbdata_id_seq OWNED BY public.pdbdata.id;


--
-- Name: protein; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.protein (
    id bigint NOT NULL,
    entry_name character varying(100) NOT NULL,
    accession character varying(100),
    name character varying(200) NOT NULL,
    family_id bigint NOT NULL,
    parent_id bigint,
    species_id bigint NOT NULL
);


ALTER TABLE public.protein OWNER TO "SH2";

--
-- Name: protein_conformation; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.protein_conformation (
    id bigint NOT NULL,
    state_id bigint NOT NULL,
    domain_id bigint NOT NULL
);


ALTER TABLE public.protein_conformation OWNER TO "SH2";

--
-- Name: protein_conformation_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.protein_conformation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.protein_conformation_id_seq OWNER TO "SH2";

--
-- Name: protein_conformation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.protein_conformation_id_seq OWNED BY public.protein_conformation.id;


--
-- Name: protein_domain; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.protein_domain (
    id bigint NOT NULL,
    domain_type_id bigint NOT NULL,
    isoform_id bigint NOT NULL,
    sequence_id bigint NOT NULL,
    parent_id bigint
);


ALTER TABLE public.protein_domain OWNER TO "SH2";

--
-- Name: protein_domain_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.protein_domain_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.protein_domain_id_seq OWNER TO "SH2";

--
-- Name: protein_domain_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.protein_domain_id_seq OWNED BY public.protein_domain.id;


--
-- Name: protein_domaintype; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.protein_domaintype (
    id bigint NOT NULL,
    slug character varying(100) NOT NULL,
    name character varying(200) NOT NULL
);


ALTER TABLE public.protein_domaintype OWNER TO "SH2";

--
-- Name: protein_domaintype_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.protein_domaintype_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.protein_domaintype_id_seq OWNER TO "SH2";

--
-- Name: protein_domaintype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.protein_domaintype_id_seq OWNED BY public.protein_domaintype.id;


--
-- Name: protein_family; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.protein_family (
    id bigint NOT NULL,
    slug character varying(100) NOT NULL,
    name character varying(200) NOT NULL,
    parent_id bigint
);


ALTER TABLE public.protein_family OWNER TO "SH2";

--
-- Name: protein_family_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.protein_family_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.protein_family_id_seq OWNER TO "SH2";

--
-- Name: protein_family_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.protein_family_id_seq OWNED BY public.protein_family.id;


--
-- Name: protein_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.protein_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.protein_id_seq OWNER TO "SH2";

--
-- Name: protein_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.protein_id_seq OWNED BY public.protein.id;


--
-- Name: protein_isoform; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.protein_isoform (
    id bigint NOT NULL,
    accession character varying(100),
    protein_id bigint NOT NULL
);


ALTER TABLE public.protein_isoform OWNER TO "SH2";

--
-- Name: protein_isoform_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.protein_isoform_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.protein_isoform_id_seq OWNER TO "SH2";

--
-- Name: protein_isoform_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.protein_isoform_id_seq OWNED BY public.protein_isoform.id;


--
-- Name: protein_segment; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.protein_segment (
    id bigint NOT NULL,
    slug character varying(100) NOT NULL,
    name character varying(50) NOT NULL,
    category character varying(50) NOT NULL,
    fully_aligned boolean NOT NULL,
    partial boolean NOT NULL,
    proteinfamily character varying(20) NOT NULL
);


ALTER TABLE public.protein_segment OWNER TO "SH2";

--
-- Name: protein_segment_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.protein_segment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.protein_segment_id_seq OWNER TO "SH2";

--
-- Name: protein_segment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.protein_segment_id_seq OWNED BY public.protein_segment.id;


--
-- Name: protein_state; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.protein_state (
    id bigint NOT NULL,
    slug character varying(20) NOT NULL,
    name character varying(100) NOT NULL
);


ALTER TABLE public.protein_state OWNER TO "SH2";

--
-- Name: protein_state_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.protein_state_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.protein_state_id_seq OWNER TO "SH2";

--
-- Name: protein_state_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.protein_state_id_seq OWNED BY public.protein_state.id;


--
-- Name: publication; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.publication (
    id bigint NOT NULL,
    journal text,
    title text,
    authors text,
    year integer,
    reference text
);


ALTER TABLE public.publication OWNER TO "SH2";

--
-- Name: publication_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.publication_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.publication_id_seq OWNER TO "SH2";

--
-- Name: publication_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.publication_id_seq OWNED BY public.publication.id;


--
-- Name: residue; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.residue (
    id bigint NOT NULL,
    sequence_number smallint NOT NULL,
    amino_acid character varying(1) NOT NULL,
    domain_id bigint NOT NULL,
    generic_number_id bigint,
    protein_segment_id bigint,
    amino_acid_three_letter character varying(3) NOT NULL
);


ALTER TABLE public.residue OWNER TO "SH2";

--
-- Name: residue_generic_number; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.residue_generic_number (
    id bigint NOT NULL,
    label character varying(12) NOT NULL,
    protein_segment_id bigint,
    scheme_id bigint NOT NULL
);


ALTER TABLE public.residue_generic_number OWNER TO "SH2";

--
-- Name: residue_generic_number_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.residue_generic_number_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.residue_generic_number_id_seq OWNER TO "SH2";

--
-- Name: residue_generic_number_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.residue_generic_number_id_seq OWNED BY public.residue_generic_number.id;


--
-- Name: residue_generic_numbering_scheme; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.residue_generic_numbering_scheme (
    id bigint NOT NULL,
    slug character varying(20) NOT NULL,
    short_name character varying(20) NOT NULL,
    name character varying(100) NOT NULL,
    parent_id bigint
);


ALTER TABLE public.residue_generic_numbering_scheme OWNER TO "SH2";

--
-- Name: residue_generic_numbering_scheme_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.residue_generic_numbering_scheme_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.residue_generic_numbering_scheme_id_seq OWNER TO "SH2";

--
-- Name: residue_generic_numbering_scheme_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.residue_generic_numbering_scheme_id_seq OWNED BY public.residue_generic_numbering_scheme.id;


--
-- Name: residue_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.residue_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.residue_id_seq OWNER TO "SH2";

--
-- Name: residue_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.residue_id_seq OWNED BY public.residue.id;


--
-- Name: sequence; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.sequence (
    id bigint NOT NULL,
    sequence text NOT NULL
);


ALTER TABLE public.sequence OWNER TO "SH2";

--
-- Name: sequence_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.sequence_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sequence_id_seq OWNER TO "SH2";

--
-- Name: sequence_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.sequence_id_seq OWNED BY public.sequence.id;


--
-- Name: species; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.species (
    id bigint NOT NULL,
    latin_name character varying(100) NOT NULL,
    common_name character varying(100) NOT NULL
);


ALTER TABLE public.species OWNER TO "SH2";

--
-- Name: species_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.species_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.species_id_seq OWNER TO "SH2";

--
-- Name: species_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.species_id_seq OWNED BY public.species.id;


--
-- Name: structure; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.structure (
    id bigint NOT NULL,
    pdb_code character varying(4) NOT NULL,
    publication_date date NOT NULL,
    resolution numeric(5,3) NOT NULL,
    publication_id bigint NOT NULL,
    structure_type_id bigint NOT NULL
);


ALTER TABLE public.structure OWNER TO "SH2";

--
-- Name: structure_domain; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.structure_domain (
    id bigint NOT NULL,
    chain_id bigint NOT NULL,
    domain_id bigint NOT NULL,
    pdbdata_id bigint NOT NULL
);


ALTER TABLE public.structure_domain OWNER TO "SH2";

--
-- Name: structure_domain_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.structure_domain_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.structure_domain_id_seq OWNER TO "SH2";

--
-- Name: structure_domain_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.structure_domain_id_seq OWNED BY public.structure_domain.id;


--
-- Name: structure_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.structure_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.structure_id_seq OWNER TO "SH2";

--
-- Name: structure_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.structure_id_seq OWNED BY public.structure.id;


--
-- Name: structure_type; Type: TABLE; Schema: public; Owner: SH2
--

CREATE TABLE public.structure_type (
    id bigint NOT NULL,
    slug character varying(50) NOT NULL,
    name character varying(20) NOT NULL
);


ALTER TABLE public.structure_type OWNER TO "SH2";

--
-- Name: structure_type_id_seq; Type: SEQUENCE; Schema: public; Owner: SH2
--

CREATE SEQUENCE public.structure_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.structure_type_id_seq OWNER TO "SH2";

--
-- Name: structure_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: SH2
--

ALTER SEQUENCE public.structure_type_id_seq OWNED BY public.structure_type.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: chain id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.chain ALTER COLUMN id SET DEFAULT nextval('public.chain_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: pdbdata id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.pdbdata ALTER COLUMN id SET DEFAULT nextval('public.pdbdata_id_seq'::regclass);


--
-- Name: protein id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein ALTER COLUMN id SET DEFAULT nextval('public.protein_id_seq'::regclass);


--
-- Name: protein_conformation id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_conformation ALTER COLUMN id SET DEFAULT nextval('public.protein_conformation_id_seq'::regclass);


--
-- Name: protein_domain id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_domain ALTER COLUMN id SET DEFAULT nextval('public.protein_domain_id_seq'::regclass);


--
-- Name: protein_domaintype id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_domaintype ALTER COLUMN id SET DEFAULT nextval('public.protein_domaintype_id_seq'::regclass);


--
-- Name: protein_family id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_family ALTER COLUMN id SET DEFAULT nextval('public.protein_family_id_seq'::regclass);


--
-- Name: protein_isoform id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_isoform ALTER COLUMN id SET DEFAULT nextval('public.protein_isoform_id_seq'::regclass);


--
-- Name: protein_segment id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_segment ALTER COLUMN id SET DEFAULT nextval('public.protein_segment_id_seq'::regclass);


--
-- Name: protein_state id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_state ALTER COLUMN id SET DEFAULT nextval('public.protein_state_id_seq'::regclass);


--
-- Name: publication id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.publication ALTER COLUMN id SET DEFAULT nextval('public.publication_id_seq'::regclass);


--
-- Name: residue id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.residue ALTER COLUMN id SET DEFAULT nextval('public.residue_id_seq'::regclass);


--
-- Name: residue_generic_number id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.residue_generic_number ALTER COLUMN id SET DEFAULT nextval('public.residue_generic_number_id_seq'::regclass);


--
-- Name: residue_generic_numbering_scheme id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.residue_generic_numbering_scheme ALTER COLUMN id SET DEFAULT nextval('public.residue_generic_numbering_scheme_id_seq'::regclass);


--
-- Name: sequence id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.sequence ALTER COLUMN id SET DEFAULT nextval('public.sequence_id_seq'::regclass);


--
-- Name: species id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.species ALTER COLUMN id SET DEFAULT nextval('public.species_id_seq'::regclass);


--
-- Name: structure id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.structure ALTER COLUMN id SET DEFAULT nextval('public.structure_id_seq'::regclass);


--
-- Name: structure_domain id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.structure_domain ALTER COLUMN id SET DEFAULT nextval('public.structure_domain_id_seq'::regclass);


--
-- Name: structure_type id; Type: DEFAULT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.structure_type ALTER COLUMN id SET DEFAULT nextval('public.structure_type_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add species	7	add_species
26	Can change species	7	change_species
27	Can delete species	7	delete_species
28	Can view species	7	view_species
29	Can add protein family	8	add_proteinfamily
30	Can change protein family	8	change_proteinfamily
31	Can delete protein family	8	delete_proteinfamily
32	Can view protein family	8	view_proteinfamily
33	Can add protein	9	add_protein
34	Can change protein	9	change_protein
35	Can delete protein	9	delete_protein
36	Can view protein	9	view_protein
37	Can add isoform	10	add_isoform
38	Can change isoform	10	change_isoform
39	Can delete isoform	10	delete_isoform
40	Can view isoform	10	view_isoform
41	Can add protein state	11	add_proteinstate
42	Can change protein state	11	change_proteinstate
43	Can delete protein state	11	delete_proteinstate
44	Can view protein state	11	view_proteinstate
45	Can add protein conformation	12	add_proteinconformation
46	Can change protein conformation	12	change_proteinconformation
47	Can delete protein conformation	12	delete_proteinconformation
48	Can view protein conformation	12	view_proteinconformation
49	Can add domain type	13	add_domaintype
50	Can change domain type	13	change_domaintype
51	Can delete domain type	13	delete_domaintype
52	Can view domain type	13	view_domaintype
53	Can add sequence	14	add_sequence
54	Can change sequence	14	change_sequence
55	Can delete sequence	14	delete_sequence
56	Can view sequence	14	view_sequence
57	Can add domain	15	add_domain
58	Can change domain	15	change_domain
59	Can delete domain	15	delete_domain
60	Can view domain	15	view_domain
61	Can add publication	16	add_publication
62	Can change publication	16	change_publication
63	Can delete publication	16	delete_publication
64	Can view publication	16	view_publication
65	Can add structure type	17	add_structuretype
66	Can change structure type	17	change_structuretype
67	Can delete structure type	17	delete_structuretype
68	Can view structure type	17	view_structuretype
69	Can add chain	18	add_chain
70	Can change chain	18	change_chain
71	Can delete chain	18	delete_chain
72	Can view chain	18	view_chain
73	Can add structure	19	add_structure
74	Can change structure	19	change_structure
75	Can delete structure	19	delete_structure
76	Can view structure	19	view_structure
77	Can add pdb data	20	add_pdbdata
78	Can change pdb data	20	change_pdbdata
79	Can delete pdb data	20	delete_pdbdata
80	Can view pdb data	20	view_pdbdata
81	Can add structure domain	21	add_structuredomain
82	Can change structure domain	21	change_structuredomain
83	Can delete structure domain	21	delete_structuredomain
84	Can view structure domain	21	view_structuredomain
85	Can add protein segment	22	add_proteinsegment
86	Can change protein segment	22	change_proteinsegment
87	Can delete protein segment	22	delete_proteinsegment
88	Can view protein segment	22	view_proteinsegment
89	Can add residue generic number	23	add_residuegenericnumber
90	Can change residue generic number	23	change_residuegenericnumber
91	Can delete residue generic number	23	delete_residuegenericnumber
92	Can view residue generic number	23	view_residuegenericnumber
93	Can add residue	24	add_residue
94	Can change residue	24	change_residue
95	Can delete residue	24	delete_residue
96	Can view residue	24	view_residue
97	Can add residue numbering scheme	25	add_residuenumberingscheme
98	Can change residue numbering scheme	25	change_residuenumberingscheme
99	Can delete residue numbering scheme	25	delete_residuenumberingscheme
100	Can view residue numbering scheme	25	view_residuenumberingscheme
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: chain; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.chain (id, "chain_ID", structure_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	protein	species
8	protein	proteinfamily
9	protein	protein
10	protein	isoform
11	protein	proteinstate
12	protein	proteinconformation
13	protein	domaintype
14	protein	sequence
15	protein	domain
16	common	publication
17	structure	structuretype
18	structure	chain
19	structure	structure
20	structure	pdbdata
21	structure	structuredomain
22	protein	proteinsegment
23	residue	residuegenericnumber
24	residue	residue
25	residue	residuenumberingscheme
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2021-11-12 14:39:23.569467+00
2	auth	0001_initial	2021-11-12 14:39:23.812332+00
3	admin	0001_initial	2021-11-12 14:39:23.870228+00
4	admin	0002_logentry_remove_auto_add	2021-11-12 14:39:23.879628+00
5	admin	0003_logentry_add_action_flag_choices	2021-11-12 14:39:23.88863+00
6	contenttypes	0002_remove_content_type_name	2021-11-12 14:39:23.91425+00
7	auth	0002_alter_permission_name_max_length	2021-11-12 14:39:23.927624+00
8	auth	0003_alter_user_email_max_length	2021-11-12 14:39:23.938774+00
9	auth	0004_alter_user_username_opts	2021-11-12 14:39:23.949998+00
10	auth	0005_alter_user_last_login_null	2021-11-12 14:39:23.96084+00
11	auth	0006_require_contenttypes_0002	2021-11-12 14:39:23.963635+00
12	auth	0007_alter_validators_add_error_messages	2021-11-12 14:39:23.973518+00
13	auth	0008_alter_user_username_max_length	2021-11-12 14:39:23.992466+00
14	auth	0009_alter_user_last_name_max_length	2021-11-12 14:39:24.011109+00
15	auth	0010_alter_group_name_max_length	2021-11-12 14:39:24.02618+00
16	auth	0011_update_proxy_permissions	2021-11-12 14:39:24.034603+00
17	auth	0012_alter_user_first_name_max_length	2021-11-12 14:39:24.044653+00
18	protein	0001_initial	2021-11-12 14:39:24.255774+00
19	protein	0002_proteinconformation_proteinstate	2021-11-12 14:39:24.371668+00
20	protein	0003_auto_20211112_1436	2021-11-12 14:39:24.553008+00
21	sessions	0001_initial	2021-11-12 14:39:24.608383+00
22	protein	0004_domain_parent	2021-11-19 12:50:45.274036+00
23	common	0001_initial	2022-01-13 12:28:57.124711+00
24	structure	0001_initial	2022-01-13 12:28:57.705203+00
25	protein	0005_proteinsegment	2022-01-13 13:26:21.72501+00
26	residue	0001_initial	2022-01-13 13:26:22.321463+00
27	residue	0002_residue_amino_acid_three_letter	2022-01-14 08:26:47.375106+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Data for Name: pdbdata; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.pdbdata (id, pdb) FROM stdin;
\.


--
-- Data for Name: protein; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.protein (id, entry_name, accession, name, family_id, parent_id, species_id) FROM stdin;
272	sh3bp2_human	P78314	SH3BP2	44	\N	4
273	abl1_human	P00519	ABL1	45	\N	4
274	abl2_human	P42684	ABL2	45	\N	4
275	bmx_human	P51813	BMX	45	\N	4
276	btk_human	Q06187	BTK	45	\N	4
277	chn1_human	P15882	CHN1	46	\N	4
278	chn2_human	P52757	CHN2	46	\N	4
279	crk_human	P46108	CRK	47	\N	4
280	crkl_human	P46109	CRKL	47	\N	4
281	csk_human	P41240	CSK	45	\N	4
282	fer_human	P16591	FER	45	\N	4
283	fes_human	P07332	FES	45	\N	4
284	fyn_human	P06241	FYN	45	\N	4
285	grap2_human	O75791	GRAP2	47	\N	4
286	grb10_human	Q13322	GRB10	44	\N	4
287	grb14_human	Q14449	GRB14	44	\N	4
288	grb2_human	P62993	GRB2	47	\N	4
289	grb7_human	Q14451	GRB7	44	\N	4
290	hck_human	P08631	HCK	45	\N	4
291	hsh2d_human	Q96JZ2	HSH2D	44	\N	4
292	jak2_human	O60674	JAK2	45	\N	4
293	syk_human	P43405	SYK	45	\N	4
294	lck_human	P06239	LCK	45	\N	4
295	matk_human	P42679	MATK	45	\N	4
296	nck1_human	P16333	NCK1	47	\N	4
297	nck2_human	P16333	NCK2	47	\N	4
298	pik3r1_human	P27986	PIK3R1	45	\N	4
299	plcg1_human	P19174	PLCG1	48	\N	4
300	ptk6_human	Q13882	PTK6	45	\N	4
301	ptpn11_human	Q06124	PTPN11	49	\N	4
302	ptpn6_human	P29350	PTPN6	49	\N	4
303	rasa1_human	P20936	RASA1	46	\N	4
304	sh2d1a_human	O60880	SH2D1A	44	\N	4
305	sh2d1b_human	O14796	SH2D1B	44	\N	4
306	sh2b1_human	Q9NRF2	SH2B1	44	\N	4
307	shc1_human	P29353	SHC1	50	\N	4
308	inpp5d_human	Q92835	INPP5D	48	\N	4
309	inppl1_human	O15357	INPPL1	48	\N	4
310	sla2_human	Q9H6Q3	SLA2	47	\N	4
311	socs2_human	O14508	SOCS2	44	\N	4
312	socs4_human	Q8WXH5	SOCS4	44	\N	4
313	socs6_human	O14544	SOCS6	44	\N	4
314	src_human	P12931	SRC	45	\N	4
315	stat5b_human	P51692	STAT5B	51	\N	4
316	stap1_human	Q9ULZ2	STAP1	51	\N	4
317	stat1_human	P42224	STAT1	51	\N	4
318	stat3_human	P40763	STAT3	51	\N	4
319	stat6_human	P42226	STAT6	51	\N	4
320	tns2_human	Q63HR2	TNS2	52	\N	4
321	txk_human	P42681	TXK	45	\N	4
322	vav2_human	P52735	VAV2	46	\N	4
323	vav1_human	P15498	VAV1	46	\N	4
324	zap70_human	P43403	ZAP70	45	\N	4
325	bcar3_human	O75815	BCAR3	53	\N	4
326	blk_human	P51451	BLK	54	\N	4
327	blnk_human	Q8WV28	BLNK	55	\N	4
328	cbl_human	P22681	CBL	56	\N	4
329	cblb_human	Q13191	CBLB	56	\N	4
330	cblc_human	Q9ULV8	CBLC	56	\N	4
331	cish_human	Q9NSE2	CISH	44	\N	4
332	clnk_human	Q7Z7G1	CLNK	57	\N	4
333	dapp1_human	Q9UN19	DAPP1	44	\N	4
334	fgr_human	P09769	FGR	54	\N	4
335	frk_human	P42685	FRK	54	\N	4
336	grap_human	Q13588	GRAP	57	\N	4
337	itk_human	Q08881	ITK	54	\N	4
338	jak1_human	P23458	JAK1	54	\N	4
339	jak3_human	P52333	JAK3	54	\N	4
340	lcp2_human	Q13094	LCP2	55	\N	4
341	lyn_human	P07948	LYN	54	\N	4
342	pik3r2_human	O00459	PIK3R2	58	\N	4
343	pik3r3_human	Q92569	PIK3R3	58	\N	4
344	plcg2_human	P16885	PLCG2	58	\N	4
345	rin1_human	Q13671	RIN1	53	\N	4
346	rin2_human	Q8WYP3	RIN2	53	\N	4
347	rin3_human	Q8TB24	RIN3	53	\N	4
348	sh2b2_human	O14492	SH2B2	44	\N	4
349	sh2b3_human	Q9UQQ2	SH2B3	44	\N	4
350	sh2d2a_human	Q9NP31	SH2D2A	44	\N	4
351	sh2d3a_human	Q9BRG2	SH2D3A	53	\N	4
352	sh2d3c_human	Q8N5H7	SH2D3C	53	\N	4
353	sh2d4a_human	Q9H788	SH2D4A	44	\N	4
354	sh2d4b_human	Q5SQS7	SH2D4B	44	\N	4
355	sh2d5_human	Q6ZV89	SH2D5	55	\N	4
356	shb_human	Q15464	SHB	44	\N	4
357	shc2_human	P98077	SHC2	55	\N	4
358	shc3_human	Q92529	SHC3	55	\N	4
359	shc4_human	Q6S5L8	SHC4	55	\N	4
360	shd_human	Q96IW2	SHD	44	\N	4
361	she_human	Q5VZ18	SHE	44	\N	4
362	shf_human	Q7M4L6	SHF	44	\N	4
363	sla_human	Q13239	SLA	57	\N	4
364	slnk_human	Q7Z4S9	SLNK	55	\N	4
365	socs1_human	O15524	SOCS1	44	\N	4
366	socs3_human	O14543	SOCS3	44	\N	4
367	socs5_human	O75159	SOCS5	44	\N	4
368	socs7_human	O14512	SOCS7	44	\N	4
369	srms_human	Q9H3Y6	SRMS	54	\N	4
370	stap2_human	Q9UGK3	STAP2	57	\N	4
371	stat2_human	P52630	STAT2	51	\N	4
372	stat4_human	Q14765	STAT4	51	\N	4
373	stat5a_human	P42229	STAT5A	51	\N	4
374	supt6h_human	Q7KZ85	SUPT6H	59	\N	4
375	tec_human	P42680	TEC	54	\N	4
376	tns1_human	Q9HBL0	TNS1	60	\N	4
377	tns3_human	Q68CZ2	TNS3	60	\N	4
378	tns4_human	Q8IZW8	TNS4	60	\N	4
379	tyk2_human	P29597	TYK2	54	\N	4
380	vav3_human	Q9UKW4	VAV3	53	\N	4
381	yes_human	P07947	YES	54	\N	4
\.


--
-- Data for Name: protein_conformation; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.protein_conformation (id, state_id, domain_id) FROM stdin;
\.


--
-- Data for Name: protein_domain; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.protein_domain (id, domain_type_id, isoform_id, sequence_id, parent_id) FROM stdin;
299	1	273	1	\N
300	1	274	2	\N
301	1	325	61	\N
302	1	326	62	\N
303	1	327	63	\N
304	1	275	3	\N
305	1	276	4	\N
306	1	328	64	\N
307	1	329	65	\N
308	1	330	66	\N
309	1	277	5	\N
310	1	278	6	\N
311	1	331	67	\N
312	1	332	68	\N
313	1	279	7	\N
314	1	280	8	\N
315	1	281	9	\N
316	1	333	69	\N
317	1	282	10	\N
318	1	283	11	\N
319	1	334	70	\N
320	1	335	71	\N
321	1	284	12	\N
322	1	336	72	\N
323	1	285	13	\N
324	1	286	14	\N
325	1	287	15	\N
326	1	288	16	\N
327	1	289	17	\N
328	1	290	18	\N
329	1	291	19	\N
330	1	308	20	\N
331	1	309	21	\N
332	1	337	73	\N
333	1	338	74	\N
334	1	292	22	\N
335	1	339	75	\N
336	1	294	23	\N
337	1	340	76	\N
338	1	341	77	\N
339	1	295	24	\N
340	1	296	25	\N
341	1	297	26	\N
342	2	298	27	\N
343	1	298	28	\N
344	2	342	78	\N
345	1	342	79	\N
346	2	343	80	\N
347	1	343	81	\N
348	2	299	29	\N
349	1	299	30	\N
350	2	344	82	\N
351	1	344	83	\N
352	1	300	31	\N
353	2	301	32	\N
354	1	301	33	\N
355	2	302	34	\N
356	1	302	35	\N
357	2	303	36	\N
358	1	303	37	\N
359	1	345	84	\N
360	1	346	85	\N
361	1	347	86	\N
362	1	306	38	\N
363	1	348	87	\N
364	1	349	88	\N
365	1	304	39	\N
366	1	305	40	\N
367	1	350	89	\N
368	1	351	90	\N
369	1	352	91	\N
370	1	353	92	\N
371	1	354	93	\N
372	1	355	94	\N
373	1	272	41	\N
374	1	356	95	\N
375	1	307	42	\N
376	1	357	96	\N
377	1	358	97	\N
378	1	359	98	\N
379	1	360	99	\N
380	1	361	100	\N
381	1	362	101	\N
382	1	363	102	\N
383	1	310	43	\N
384	1	364	103	\N
385	1	365	104	\N
386	1	311	44	\N
387	1	366	105	\N
388	1	312	45	\N
389	1	367	106	\N
390	1	313	46	\N
391	1	368	107	\N
392	1	314	47	\N
393	1	369	108	\N
394	1	316	48	\N
395	1	370	109	\N
396	1	317	49	\N
397	1	371	110	\N
398	1	318	50	\N
399	1	372	111	\N
400	1	373	112	\N
401	1	315	51	\N
402	1	319	52	\N
403	1	374	113	\N
404	2	293	53	\N
405	1	293	54	\N
406	1	375	114	\N
407	1	376	115	\N
408	1	320	55	\N
409	1	377	116	\N
410	1	378	117	\N
411	1	321	56	\N
412	1	379	118	\N
413	1	323	57	\N
414	1	322	58	\N
415	1	380	119	\N
416	1	381	120	\N
417	2	324	59	\N
418	1	324	60	\N
\.


--
-- Data for Name: protein_domaintype; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.protein_domaintype (id, slug, name) FROM stdin;
1	N	N-terminal
2	C	C-terminal
\.


--
-- Data for Name: protein_family; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.protein_family (id, slug, name, parent_id) FROM stdin;
44	sigreg	SigReg	\N
45	kinases	Kinases	\N
46	small_gtpase_sig	Small_GTPase_sig	\N
47	adaptors	Adaptors	\N
48	phoslip_second_mess	PhosLip_second_mess	\N
49	phosphatases	Phosphatases	\N
50	scaffolds	Scaffolds	\N
51	transcription	Transcription	\N
52	cytoskeletal_reg	Cytoskeletal_reg	\N
53	small gtpase	Small GTPase	\N
54	kinase	Kinase	\N
55	scaffold	Scaffold	\N
56	ubiquitination	Ubiquitination	\N
57	adaptor	Adaptor	\N
58	phospholipid second messenger	Phospholipid Second Messenger	\N
59	chromatin remodeling	Chromatin Remodeling	\N
60	cytoskeletal	Cytoskeletal	\N
\.


--
-- Data for Name: protein_isoform; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.protein_isoform (id, accession, protein_id) FROM stdin;
272	P78314-1	272
273	P00519-1	273
274	P42684-1	274
275	P51813-1	275
276	Q06187-1	276
277	P15882-1	277
278	P52757-1	278
279	P46108-1	279
280	P46109-1	280
281	P41240-1	281
282	P16591-1	282
283	P07332-1	283
284	P06241-1	284
285	O75791-1	285
286	Q13322-1	286
287	Q14449-1	287
288	P62993-1	288
289	Q14451-1	289
290	P08631-1	290
291	Q96JZ2-1	291
292	O60674-1	292
293	P43405-1	293
294	P06239-1	294
295	P42679-1	295
296	P16333-1	296
297	P16333-1	297
298	P27986-1	298
299	P19174-1	299
300	Q13882-1	300
301	Q06124-1	301
302	P29350-1	302
303	P20936-1	303
304	O60880-1	304
305	O14796-1	305
306	Q9NRF2-1	306
307	P29353-1	307
308	Q92835-1	308
309	O15357-1	309
310	Q9H6Q3-1	310
311	O14508-1	311
312	Q8WXH5-1	312
313	O14544-1	313
314	P12931-1	314
315	P51692-1	315
316	Q9ULZ2-1	316
317	P42224-1	317
318	P40763-1	318
319	P42226-1	319
320	Q63HR2-1	320
321	P42681-1	321
322	P52735-1	322
323	P15498-1	323
324	P43403-1	324
325	O75815-1	325
326	P51451-1	326
327	Q8WV28-1	327
328	P22681-1	328
329	Q13191-1	329
330	Q9ULV8-1	330
331	Q9NSE2-1	331
332	Q7Z7G1-1	332
333	Q9UN19-1	333
334	P09769-1	334
335	P42685-1	335
336	Q13588-1	336
337	Q08881-1	337
338	P23458-1	338
339	P52333-1	339
340	Q13094-1	340
341	P07948-1	341
342	O00459-1	342
343	Q92569-1	343
344	P16885-1	344
345	Q13671-1	345
346	Q8WYP3-1	346
347	Q8TB24-1	347
348	O14492-1	348
349	Q9UQQ2-1	349
350	Q9NP31-1	350
351	Q9BRG2-1	351
352	Q8N5H7-1	352
353	Q9H788-1	353
354	Q5SQS7-1	354
355	Q6ZV89-1	355
356	Q15464-1	356
357	P98077-1	357
358	Q92529-1	358
359	Q6S5L8-1	359
360	Q96IW2-1	360
361	Q5VZ18-1	361
362	Q7M4L6-1	362
363	Q13239-1	363
364	Q7Z4S9-1	364
365	O15524-1	365
366	O14543-1	366
367	O75159-1	367
368	O14512-1	368
369	Q9H3Y6-1	369
370	Q9UGK3-1	370
371	P52630-1	371
372	Q14765-1	372
373	P42229-1	373
374	Q7KZ85-1	374
375	P42680-1	375
376	Q9HBL0-1	376
377	Q68CZ2-1	377
378	Q8IZW8-1	378
379	P29597-1	379
380	Q9UKW4-1	380
381	P07947-1	381
\.


--
-- Data for Name: protein_segment; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.protein_segment (id, slug, name, category, fully_aligned, partial, proteinfamily) FROM stdin;
\.


--
-- Data for Name: protein_state; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.protein_state (id, slug, name) FROM stdin;
\.


--
-- Data for Name: publication; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.publication (id, journal, title, authors, year, reference) FROM stdin;
\.


--
-- Data for Name: residue; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.residue (id, sequence_number, amino_acid, domain_id, generic_number_id, protein_segment_id, amino_acid_three_letter) FROM stdin;
\.


--
-- Data for Name: residue_generic_number; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.residue_generic_number (id, label, protein_segment_id, scheme_id) FROM stdin;
\.


--
-- Data for Name: residue_generic_numbering_scheme; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.residue_generic_numbering_scheme (id, slug, short_name, name, parent_id) FROM stdin;
\.


--
-- Data for Name: sequence; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.sequence (id, sequence) FROM stdin;
1	KNGQGWVPSNYITPVNSLEKHSWYHGPVSRNAAEYLLSSGINGSFLVRESESSPGQRSISLRYEGRVYHYRINTASDGKLYVSSESRFNTLAELVHHHSTVADGLITTLHYPAPKRNKPTVYGV
2	KNGQGWVPSNYITPVNSLEKHSWYHGPVSRSAAEYLLSSLINGSFLVRESESSPGQLSISLRYEGRVYHYRINTTADGKVYVTAESRFSTLAELVHHHSTVADGLVTTLHYPAPKCNKPTVYGV
3	KISWEFPESSSSEEEENLDDYDWFAGNISRSQSEQLLRQKGKEGAFMVRNSSQVGMYTVSLFSKAVNDKKGTVKHYHVHTNAENKLYLAENYCFDSIPKLIHYHQHNSAGMITRLRHPVSTKANKVPDSV
4	GQEGYIPSNYVTEAEDSIEMYEWYSKHMTRSQAEQLLKQEGKEGGFIVRDSSKAGKYTVSVFAKSTGDPQGVIRHYVVCSTPQSQYYLAEKHLFSTIPELINYHQHNSAGLISRLKYPVSQQNKNAPSTA
5	APHPRRITCTCEVENRPKYYGREFHGMISREAADQLLIVAEGSYLIRESQRQPGTYTLALRFGSQTRNFRLYYDGKHFVGEKRFESIHDLVTDGLITLYIETKAAEYIAKMTINPIYEHV
6	APRPKRIICPREVENRPKYYGREFHGIISREQADELLGGVEGAYILRESQRQPGCYTLALRFGNQTLNYRLFHDGKHFVGEKRFESIHDLVTDGLITLYIETKAAEYISKMTTNPIYEHI
7	MAGNFDSEERSSWYWGRLSRQEAVALLQGQRHGVFLVRDSSTSPGDYVLSVSENSRVSHYIINSSGPRPPVPPSPAQPPPGVSPSRLRIGDQEFDSLPALLEFYKIHYWDTTTLIEPVSRSRQGSGVILR
8	MSSARFDSSDRSAWYMGPVSRQEAQTRLQGQRHGMFLVRDSSTCPGDYVLSVSENSRVSHYIINSLPNRRFKIGDQEFDHLPALLEFYKIHYLDTTTLIEPAPRYPSPPMGSVS
9	IPANYVQKREGVKAGTKLSLMPWFHGKITREQAERLLYPPETGLFLVRESTNYPGDYTLCVSCDGKVEHYRIMYHASKLSIDEEVYFENLMQLVEHYTSDADGLCTRLIKPKVMEGTVAAQDE
10	AVGSSALSDMISISEKPLAEQDWYHGAIPRIEAQELLKKQGDFLVRESHGKPGEYVLSVYSDGQRRHFIIQYVDNMYRFEGTGFSNIPQLIDHHYTTKQVITKKSGVVLLNPIPKDKKWI
11	KFSLPPPLQLIPEVQKPLHEQLWYHGAIPRAEVAELLVHSGDFLVRESQGKQEYVLSVLWDGLPRHFIIQSLDNLYRLEGEGFPSIPLLIDHLLSTQQPLTKKSGVVLHRAVPKDKWVL
12	TGETGYIPSNYVAPVDSIQAEEWYFGKLGRKDAERQLLSFGNPRGTFLIRESETTKGAYSLSIRDWDDMKGDHVKHYKIRKLDNGGYYITTRAQFETLQQLVQHYSERAAGLCCRLVVPCHKGMPRLTDLS
13	KAELGSQEGYVPKNFIDIQFPKWFHEGLSRHQAENLLMGKEVGFFIIRASQSSPGDFSISVRHEDDVQHFKVMRDNKGNYFLWTEKFPSLNKLVDYYRTNSISRQKQIFLRDRTREDQGHRGN
14	ILGSQSPLHPSTLSTVIHRTQHWFHGRISREESHRIIKQQGLVDGLFLLRDSQSNPKAFVLTLCHHQKIKNFQILPCEDDGQTFFSLDDGNTKFSDLIQLVDFYQLNKGVLPCKLKHHCIRVAL
15	HGSPTASSQSSATNMAIHRSQPWFHHKISRDEAQRLIIQQGLVDGVFLVRDSQSNPKTFVLSMSHGQKIKHFQIIPVEDDGEMFHTLDDGHTRFTDLIQLVEFYQLNKGVLPCKLKHYCARIAL
16	KAELNGKDGFIPKNYIEMKPHPWFFGKIPRAKAEEMLSKQRHDGAFLIRESESAPGDFSLSVKFGNDVQHFKVLRDGAGKYFLWVVKFNSLNELVDYHRSTSVSRNQQIFLRDIEQVPQQPTYV
17	RLSLPMPASGTSLSAAIHRTQLWFHGRISREESQRLIGQQGLVDGLFLVRESQRNPQGFVLSLCHLQKVKHYLILPSEEEGRLYFSMDDGQTRFTDLLQLVEFHQLNRGILPCLLRHCCTRVAL
18	TRKEGYIPSNYVARVDSLETEEWFFKGISRKDAERQLLAPGNMLGSFMIRDSETTKGSYSLSVRDYDPRQGDTVKHYKIRTLDNGGFYISPRSTFSTLQELVDHYKKGNDGLCQKLSVPCMSSKPQKPWEK
19	PPRLDWFVHTQMGQLAQDGVPEWFHGAISREDAENLLESQPLGSFLIRVSHSHVGYTLSYKAQSSCCHFMVKLLDDGTFMIPGEKVAHTSLDALVTFHQQKPIEPRRELLTQPCRQKDPANVDYE
20	MVPCWNHGNITRSKAEELLSRTGKGTSFLVRASESISRAYALCVLYRNCVYTYRILPNEDDKFTVQASEGVSMRFFTKLDQLIEFYKKENMGMGLVTHLQYPVPLEEEDTGD
21	MASACGAPGPGGALGSQAPSWYHRDLSRAAAEELLARAGRDGSFLVRDSESVAGAFALCVLYQKHVHTYRILPDGEDFLAVQTSQGVPVRRFQTLGELIGLYAQPNQGLVCALLLPVEGEREPDPPDD
22	ADAHHYLCKEVAPPAVLENIQSNCHGPISMDFAISKLKKAGNQTGLYVLRCSPKDFNKYFLTFAVERENVIEYKHCLITKNENEEYNLSGTKKNFSSLKDLLNCYQMETVRSDNIIFQFTKCCPPKPKDKS
23	TGQEGFIPFNFVAKANSLEPEPWFFKNLSRKDAERQLLAPGNTHGSFLIRESESTAGSFSLSVRDFDQNQGEVVKHYKIRNLDNGGFYISPRITFPGLHELVRHYTNASDGLCTRLSRPCQTQKPQKPWWE
24	LAAGALREREALSADPKLSLMPWFHGKISGQEAVQQLQPPEDGLFLVRESARHPGDYVLCVSFGRDVIHYRVLHRDGHLTIDEAVFFCNLMDMVEHYSKDKGAICTKLVRPKRKHGTKSAEEE
25	EPSPPQCDYIRPSLTGKFAGNPWYYGKVTRHQAEMALNERGHEGDFLIRDSESSPNDFSVSLKAQGKNKHFKVQLKETVYCIGQRKFSTMEELVEHYKKAPIFTSEQGEKLYLVKHLS
26	PAHAPQISYTGPSSSGRFAGREWYYGNVTRHQAQCALNERGVEGDFLIRDSESSPSDFSVSLKASGKNKHFKVQLVDNVYCIGQRRFHTMDELVEHYKKAPIFTSEHGEKLYLVRALQ
27	NTEDQYSLVEDDEDLPHHDEKTWNVGSSNRNKAENLLRGKRDGTFLVRESSKQGCYACSVVVDGEVKHCVINKTATGYGFAEPYNLYSSLKELVLHYQHTSLVQHNDSLNVTLAYPVYAQQRR
28	PPKPTTVANNGMNNNMSLQDAEWYWGDISREEVNEKLRDTADGTFLVRDASTKMHGDYTLTLRKGGNNKLIKIFHRDGKYGFSDPLTFSSVVELINHYRNESLAQYNPKLDVKLLYPVSKYQQD
29	CNEFEMRLSEPVPQTNAHESKEWYHASLTRAQAEHMLMRVPRDGAFLVRKRNEPNSYAISFRAEGKIKHCRVQQEGQTVMLGNSEFDSLVDLISYYEKHPLYRKMKLRYPINEEALEKIGTA
30	GNEDEEEPKEVSSSTELHSNEKWFHGKLGAGRDGRHIAERLLTEYCIETGAPDGSFLVRESETFVGDYTLSFWRNGKVQHCRIHSRQDAGTPKFFLTDNLVFDSLYDLITHYQQVPLRCNEFEMRLSEPVPQTNAHES
31	AVAQGYVPHNYLAERETVESEPWFFGCISRSEAVRRLQAEGNATGAFLIRVSEKPSADYVLSVRDTQAVRHYKIWRRAGGRLHLNEAVSFLSLPELVNYHRAQSLSHGLRLAAPCRKHEPEPLPHW
32	EKNGDVIELKYPLNCADPTSERWFHGHLSGKEAEKLLTEKGKHGSFLVRESQSHPGDFVLSVRTGDDKGESNDGKSKVTHVMIRCQELKYDVGGGERFDSLTDLVEHYKKNPMVETLGTVLQLKQPLNTTRINA
33	MTSRRWFHPNITGVEAENLLLTRGVDGSFLARPSKSNPGDFTLSVRRNGAVTHIKIQNTGDYYDLYGGEKFATLAELVQYYMEHHGQLKEKNGDVIELKYPLNCADP
34	DRDGTIIHLKYPLNCSDPTSERWYHGHMSGGQAETLLQAKGEPWTFLVRESLSQPGDFVLSVLSDQPKAGPGSPLRVTHIKVMCEGGRYTVGGLETFDSLTDLVEHFKKTGIEEASGAFVYLRQPYYATRVNA
35	MVRWFHRDLSGLDAETLLKGRGVHGSFLARPSRKNQGDFSLSVRVGDQVTHIRIQNSGDFYDLYGGEKFATLTELVEYYTQQQGVLQDRDGTIIHLKYPLNCSDP
36	GLIVEDLVEEVGREEDPHEGKIWFHGKISKQEAYNLLMTVGQVCSFLVRPSDNTPGDYSLYFRTNENIQRFKICPTPNNQFMMGGRYYNSIGDIIDHYRKEQIVEGYYLKEPVPMQDQEQVLND
37	LDGPEYEEEEVAIPLTAPPTNQWYHGKLDRTIAEERLRQAGKSGSYLIRESDRRPGSFVLSFLSQMNVVNHFRIIAMCGDYYIGGRRFSSLSDLIGYYSHVSCLLKGEKLLYPVAPPEPVEDRR
38	GSFLFQGEPEGGEGDQPLSGYPWFHGMLSRLKAAQLVLTGGTGSHGVFLVRQSETRRGEYVLTFNFQGKAKHLRLSLNEEGQCRVQHLWFQSIFDMLEHFRVHPIPLESGGSSDVVLVSYVPSSQR
39	MDAVAVYHGKISRETGEKLLLATGLDGSYLLRDSESVPGVYCLCVLYHGYIYTYRVSQTETGSWSAETAPGVHKRYFRKIKNLISAFQKPDQGIVIPLQYPVEKKSSARSTQGTTGI
40	MDLPYYHGRLTKQDCETLLLKEGVDGNFLLRDSESIPGVLCLCVSFKNIVYTYRIFREKHGYYRIQTAEGSPKQVFPSLKELISKFEKPNQGMVVHLLKPIKRTSPSLRWRGLKLELE
41	SQADTGGDDSDEDYEKVPLPNSVFVNTTESCEVERLFKATSPRGEPQDGLYCIRNSSTKSGKVLVVWDETSNKVRNYRIFEKDSKFYLEGEVLFVSVGSMVEHYHTHVLPSHQSLLLRHPYGYTGPR
42	DALRVPPPPQSVSMAEQLRGEPWFHGKLSRREAEALLQLNGDFLVRESTTTPGQYVLTGLQSGQPKHLLLVDPEGVVRTKDHRFESVSHLISYHMDNHLPIISAGSELCLQQPVERKL
43	LSEVSGREYNIPSVHVAKVSHGWLYEGLSREKAEELLLLPGNPGGAFLIRESQTRRGSYSLSVRLSRPASWDRIRHYRIHCLDNGWLYISPRLTFPSLQALVDHYSELADDICCLLKEPCVLQRAGPLPGK
44	AEEPSPQAARLAKALRELGQTGWYWGSMTVNEAKEKLKEAPEGTFLIRDSSHSDYLLTISVKTSAGPTNLRIEYQDGKFRLDSIICVKSKLKQFDSVVHLIDYYVQMCKDKRTGPEAPRNGTVHLYLTKP
45	YHTQIDYVHCLVPDLLQINNNPCYWGVMDKYAAEALLEGKPEGTFLLRDSAQEDYLFSVSFRRYSRSLHARIEQWNHNFSFDAHDPCVFHSPDITGLLEHYKDPSACMFFEPLLSTPLIRTFPFSLQ
46	QSSGPMVVTSLTEELKKLAKQGWYWGPITRWEAEGKLANVPDGSFLVRDSSDDRYLLSLSFRSHGKTLHTRIEHSNGRFSFYEQPDVEGHTSIVDLIEHSIRDSENGAFCYSRSRLPGSATYPVRL
47	TGQTGYIPSNYVAPSDSIQAEEWYFGKITRRESERLLLNAENPRGTFLVRESETTKGAYCLSVSDFDNAKGLNVKHYKIRKLDSGGFYITSRTQFNSLQQLVAYYSKHADGLCHRLTTVCPTSKPQTQGLA
48	STSVEKEKEPTEDYVDVLNPMPACFYTVSRKEATEMLQKNPSLGNMILRPGSDSRNYSITIRQEIDIPRIKHYKVMSVGQNYTIELEKPVTLPNLFSVIDYFVKETRGNLRPFICSTDENTGQEPSME
49	WLWIESILELIKKHLLPLWNDGCIMGFISKERERALLKDQQPGTFLLRFSESSREGAITFTWVERSQNGGEPDFHAVEPYTKKELSAVTFPDIIRNYKVMAAENIPENPLKYLYPNIDKDHAFGKYYSRPKEAPEPME
50	FWVWLDNIIDLVKKYILALWNEGYIMGFISKERERAILSTKPPGTFLLRFSESSKEGGVTFTWVEKDISGKTQIQSVEPYTKQQLNNMSFAEIIMGYKIMDATNILVSPLVYLYPDIPKEEAF
51	GRNYTFWQWFDGVMEVLKKHLKPHWNDGAILGFVNKQQAHDLLINKPDGTFLLRFSDSEIGGITIAWKFDSQERMFWNLMPFTTRDFSIRSLADRLGDLNYLIYVFPDRPKDEVYSKYYTPVPCESATAKA
52	GVLDLTKRCLRSYWSDRLIIGFISKQYVTSLLLNEPDGTFLLRFSDSEIGGITIAHVIRGQDGSPQIENIQPFSAKDLSIRSLGDRIRDLAQLKNLYPKKPKDEAFRSHYKPEQMGKD
53	AIISQKPQLEKLIATTAHEKMPWFHGKISREESEQIVLIGSKTNGKFLIRARDNNGSYALCLLHEGKVLHYRIDKDKTGKLSIPEGKKFDTLWQLVEHYSYKADGLLRVLTVPCQKIGTQGNVNF
54	MASSGMADSANHLPFFFGNITREEAEDYLVQGGMSDGLYLLRQSRNYLGGFALSVAHGRKAHHYTIERELNGTYAIAGGRTHASPADLCHYHSQESDGLVCLLKKPFNRPQGVQPKTG
55	TPEPPTQESQSNVKFVQDTSKFWYKPHLSRDQAIALLKDKDPGAFLIRDSHSFQGAYGLALKVATPPPSAQPWKGDPVEQLVRHFLIETGPKGVKIKGCPSEPYFGSLSALVSQHSISPISLPCCLRILSKDPLEETPEAP
56	NEGLIPSNYVTENKITNLEIYEWYHRNITRNQAEHLLRQESKEGAFIVRDSRHLGSYTISVFMGARRSTEAAIKHYQIKKNDSGQWYVAERHAFQSIPELIWYHQHNAAGLMTRLRYPVGLMGSCLPATA
57	WFPCNRVKPYVHGPPQDLSVHLWYAGPMERAGAESILANRSDGTFLVRQRVKDAAEFAISIKYNVEVKHIKIMTAEGLYRITEKKAFRGLTELVEFYQQNSLKDCFKSLDTTLQFPFKEPEKR
58	PVDGRPPISRPPSREIDYTAYPWFAGNMERQQTDNLLKSHASGTYLIRERPAEAERFAISIKFNDEVKHIKVVEKDNWIHITEAKKFDSLLELVEYYQCHSLKESFKQLDTTLKYPYKSRERS
59	AIISQAPQVEKLIATTAHERMPWYHSSLTREEAERKLYSGAQTDGKFLLRPRKEQGTYALSLIYGKTVYHYLISQDKAGKYCIPEGTKFDTLWQLVEYLKLKADGLIYCLKEACPNSSASNASGA
60	MPDPAAHLPFFYGSISRAEAEEHLKLAGMADGLFLLRQCLRSLGGYVLSLVHDVRFHHFPIERQLNGTYAIAGGKAHCGPAELCEFYSRDPDGLPCNLRKPCNRPSGLEPQPG
61	EKLKKELEEELLLSSEDLRSHAWYHGRIPRQVSENLVQRDGDFLVRDSLSSPGNFVLTCQWKNLAQHFKINRTVLRLSEAYSRVQYQFEMESFDSIPGLVRCYVGNRRPISQQSGAIIFQPINRTVPLR
62	TGREGYVPSNFVARVESLEMERWFFRSQGRKEAERQLLAPINKAGSFLIRESETNKGAFSLSVKDVTTQGELIKHYKIRCLDEGGYYISPRITFPSLQALVQHYSKKGDGLCQRLTLPCVRPAPQNPWAQ
63	FSSNSTISEQEAGVLCKPWYAGACDRKSAEEALHRSNKDGSFLIRKSSGHDSKQPYTLVVFFNKRVYNIPVRFIEATKQYALGRKKNGEEYFGSVAEIIRNHQHSPLVLIDSQNNTKDSTRLKYAVKV
64	TRLFQPWSSLLRNWNSLAVTHPGYMAFLTYDEVKARLQKFIHKPGSYIFRLSCTRLGQWAIGYVTADGNILQTIPHNKPLFQALIDGFREGFYLFPDGRNQNPDLTGLCEPTPQDHIKVTQEQYELYCEMGSTFQLCK
65	TRLFQPWGSILRNWNFLAVTHPGYMAFLTYDEVKARLQKYSTKPGSYIFRLSCTRLGQWAIGYVTGDGNILQTIPHNKPLFQALIDGSREGFYLYPDGRSYNPDLTGLCEPTPHDHIKVTQEQYELYCEMGSTFQLCK
66	TRLFQPWPTLLKNWQLLAVTHPGYMAFLTYDEVQERLQACRDKPGSYIFRPSCTRLGQWAIGYVSSDGSILQTIPANKPLSQVLLEGQKDGFYLYPDGKTHNPDLTELGQAEPQQRIHVSEEQLQLYWAMDSTFELCK
67	VLDPEEDLLCIAKTFSYLRESGWYWGSITASEARQHLQKMPEGTFLVRDSTHPSYLFTLSVKTTRGPTNVRIEYADSSFRLDSNCLSRPRILAFPDVVSLVQHYVASCTADTRSDSPDPAPTPALPMPKE
68	KYTSWRPPFPKRSDRKDVQHNEWYIGEYSRQAVEEAFMKENKDGSFLVRDCSTKSKEEPYVLAVFYENKVYNVKIRFLERNQQFALGTGLRGDEKFDSVEDIIEHYKN
69	TQDPSDLWSRSDGEAELLQDLGWYHGNLTRHAAEALLLSNGCDGSYLLRDSNETTGLYSLSVRAKDSVKHFHVEYTGYSFKFGFNEFSSLKDFVKHFANQPLIGSETGTLMVLKHPYPRKVEE
70	SGKTGCIPSNYVAPVDSIQAEEWYFGKIGRKDAERQLLSPGNPQGAFLIRESETTKGAYSLSIRDWDQTRGDHVKHYKIRKLDMGGYYITTRVQFNSVQELVQHYMEVNDGLCNLLIAPCTIMKPQTLGLA
71	QQLQGYIPSNYVAEDRSLQAEPWFFGAIGRSDAEKQLLYSENKTGSFLIRESESQKGEFSLSVLDGAVVKHYRIKRLDEGGFFLTRRRIFSTLNEFVSHYTKTSDGLCVKLGKPCLKIQVPAPFDL
72	KAELRGVEGFIPKNYIRVKPHPWYSGRISRQLAEEILMKRNHLGAFLIRESESSPGEFSVSVNYGDQVQHFKVLREASGKYFLWEEKFNSLNELVDFYRTTTIAKKRQIFLRDEEPLLKSPGAC
73	NGHEGYVPSSYLVEKSPNNLETYEWYNKSISRDKAEKLLLDTGKEGAFMVRDSRTAGTYTVSVFTKAVVSENNPCIKHYHIKETNDNPKRYYVAEKYVFDSIPLLINYHQHNGGGLVTRLRYPVCFGRQKAPVTA
74	ADAHHYLCTDVAPPLIVHNIQNGCHGPICTEYAINKLRQEGSEEGMYVLRWSCTDFDNILMTVTCFEKSEQVQGAQKQFKNFQIEVQKGRYSLHGSDRSFPSLGDLMSHLKKQILRTDNISFMLKRCCQPKPREIS
75	TDSQHFFCKEVAPPRLLEEVAEQCHGPITLDFAINKLKTGGSRPGSYVLRRSPQDFDSFLLTVCVQNPLGPDYKGCLIRRSPTGTFLLVGLSRPHSSLRELLATCWDGGLHVDGVAVTLTSCCIPRPKEKS
76	LPLPNKPRPPSPAEEENSLNEEWYVSYITRPEAEAALRKINQDGTFLVRDSSKKTTTNPYVLMVLYKDKVYNIQIRYQKESQVYLLGTGLRGKEDFLSVSDIIDYFRKMPLLIDGKNRGSRYQCTLTHAAGY
77	TKKEGFIPSNYVAKLNTLETEEWFFKDITRKDAERQLLAPGNSAGAFLIRESETLKGSFSLSVRDFDPVHGDVIKHYKIRSLDNGGYYISPRITFPCISDMIKHYQKQADGLCRRLEKACISPKPQKPWDK
78	ETEDQYALMEDEDDLPHHEERTWYVGKINRTQAEEMLSGKRDGTFLIRESSQRGCYACSVVVDGDTKHCVIYRTATGFGFAEPYNLYGSLKELVLHYQHASLVQHNDALTVTLAHPVRAPGPG
79	PKPPKAKPAPTVLANGGSPPSLQDAEWYWGDISREEVNEKLRDTPDGTFLVRDASSKIQGEYTLTLRKGGNNKLIKVFHRDGHYGFSEPLTFCSVVDLINHYRHESLAQYNAKLDTRLLYPVSKYQQD
80	DADENYFINEEDENLPHYDEKTWFVEDINRVQAEDLLYGKPDGAFLIRESSKKGCYACSVVADGEVKHCVIYSTARGYGFAEPYNLYSSLKELVLHYQQTSLVQHNDSLNVRLAYPVHAQMPS
81	KPMTSAVPNGMKDSSVSLQDAEWYWGDISREEVNDKLRDMPDGTFLVRDASTKMQGDYTLTLRKGGNNKLIKIYHRDGKYGFSDPLTFNSVVELINHYHHESLAQYNPKLDVKLMYPVSRYQQD
82	CAEFELRLTDPVPNPNPHESKPWYYDSLSRGEAEDMLMRIPDGAFLIRKREGSDSYAITFRARGKVKHCRINRDGRHFVLGTSAYFESLVELVSYYEKHSLYRKMRLRYPVTPELLERYNME
83	EQTMEEEVPQDIPPTELHFGEKWFHKKVEKRTSAEKLLQEYCMETGGKDGTFLVRESETFPNDYTLSFWRSGRVQHCRIRSTMEGGTLKYYLTDNLRFRRMYALIQHYRETHLPCAEFELRLTDPVPNPNPHES
84	QRPGRVVSLRERLLLTRPVWLQLQANAAAALHMLRTEPPGTFLVRKSNTRQCQALCMRLPEASGPSFVSSHYILESPGGVSLEGSELMFPDLVQLICAYCHTRDILLLPLQLPRAIHHAATHKELEAISHLGIE
85	SGYDSLSNRLSILDRLLHTHPIWLQLSLSEEEAAEVLQAQPPGIFLVHKSTKMQKKVLSLRLPCEFGAPLKEFAIKESTYTFSLEGSGISFADLFRLIAFYCISRDVLPFTLKLPYAISTAKSEAQL
86	KNCLPHRRGISILEKLIKTCPVWLQLSLGQAEVARILHRVVAGMFLVRRDSSSKQLVLCVHFPSLNESSAEVLEYTIKEEKSILYLEGSALVFEDIFRLIAFYCVSRDLLPFTLRLPQAILEASSFTDL
87	TGEQGAETDPEAEPELELSDYPWFHGTLSRVKAAQLVLAGGPRNHGLFVIRQSETRPGEYVLTFNFQGKAKHLRLSLNGHGQCHVQHLWFQSVLDMLRHFHTHPIPLESGGSADITLRSYVRAQDP
88	ASPGGLLDPACQKTDHFLSCYPWFHGPISRVKAAQLVQLQGPDAHGVFLVRQSETRRGEYVLTFNFQGIAKHLRLSLTERGQCRVQHLHFPSVVDMLHHFQRSPIPLECGAACDVRLSSYVVVVSQ
89	ETRAWFQKTQAHWLLQHGAAPAWFHGFITRREAERLLEPKPQGCYLVRFSESAVTFVLTYRSRTCCRHFLLAQLRDGRHVVLGEDSAHARLQDLLLHYTAHPLSPYGETLTEPLARQTPEPAGL
90	MQVPQDGEDLAGQPWYHGLLSRQKAEALLQQDGDFLVRASGSRGGNPVISCRWRGSALHFEVFRVALRPRPGRPTALFQLEDEQFPSIPALVHSYMTGRRPLSQATGAVVSRPVTWQGPLR
91	EKLHKELEEELKLSSTDLRSHAWYHGRIPREVSETLVQRNGDFLIRDSLTSLGDYVLTCRWRNQALHFKINKVVVKAGESYTHIQYLFEQESFDHVPALVRYHVGSRKAVSEQSGAIIYCPVNRTFPLR
92	WFKEEQLPLRAGYQKTSDTIAPWFHGILTLKKANELLLSTGMPGSFLIRVSERIKGYALSYLSEDGCKHFLIDASADAYSFLGVDQLQHATLADLVEYHKEEPITSLGKELLLYPCGQQDQLPDY
93	AGFERNTKFIAAPWFHGIISREDAEALLENMTEGAFLVRVSEKIWGYTLSYRLQKGFKHFLVDASGDFYSFLGVDPNRHATLTDLVDFHKEEIITVSGGELLQEPCGQR
94	VESEGSLTENIWAFAGISRPCALALLRRDVLGAFLLWPELGASGQWCLSVRTQCGVVPHQVFRNHLGRYCLEHLPAEFPSLEALVENHAVTERSLFCPLDMGRLN
95	SPEFCGILGERVDPAVPLEKQIWYHGAISRGDAENLLRLCKECSYLVRNSQTSKHDYPLSLRSNQGFMHMKLAKTKEKYVLGQNSPPFDSVPEVIHYYTTRKLPIKGAEHLSLLYPVAVRTL
96	WPSPPTRRAPVAPTEEQLRQEPWYHGRMSRRAAERMLRADGDFLVRDSVTNPGQYVLTGMHAGQPKHLLLVDPEGVVRTKDVLFESISHLIDHHLQNGQPIVAAESELHLRGVVSREP
97	CISPVSPRAPDAKMLEELQAETWYQGEMSRKEAEGLLEKDGDFLVRKSTTNPGSFVLTGMHNGQAKHLLLVDPEGTIRTKDRVFDSISHLINHHLESSLPIVSAGSELCLQQPVERKQ
98	ATAQPASSHSLPHIKQQLWSEECYHGKLSRKAAESLLVKDGDFLVRESATSPGQYVLSGLQGGQAKHLLLVDPEGKVRTKDHVFDNVGHLIRYHMDNSLPIISSGSEVSLKQPVRKDNNP
99	PPPRSPQPAERVDPALPLEKQPWFHGPLNRADAESLLSLCKEGSYLVRLSETNPQDCSLSLRSSQGFLHLKFARTRENQVVLGQHSGPFPSVPELVLHYSSRPLPVQGAEHLALLYPVVTQTP
100	GLPLEKQPWYHGAISRAEAESRLQPCKEAGYLVRNSESGNSRYSIALKTSQGCVHIIVAQTKDNKYTLNQTSAVFDSIPEVVHYYSNEKLPFKGAEHMTLL
101	SMEPSSPLGEWTDPALPLENQVWYHGAISRTDAENLLRLCKEASYLVRNSETSKNDFSLSLKSSQGFMHMKLSRTKEHKYVLGQNSPPFSSVPEIVHHYASRKLPIKGAEHMSLLYPVAIRTL
102	ISLSTGRESYIPGICVARVYHGWLFEGLGRDKAEELLQLPDTKVGSFMIRESETKKGFYSLSVRHRQVKHYRIFRLPNNWYYISPRLTFQCLEDLVNHYSEVADGLCCVLTTPCLTQSTAAPAVR
103	AEDSDLLTQPWYSGNCDRYAVESALLHLQKDGAYTVRPSSGPHGSQPFTLAVLLRGRVFNIPIRRLDGGRHYALGREGRNREELFSSVAAMVQHFMWHPLPLVDRHSGSRELT
104	FRTFRSHADYRRITRASALLDACGFYWGPLSVHGAHERLRAEPVGTFLVRDSRQRNCFFALSVKMASGPTSIRVHFQAGRFHLDGSRESFDCLFELLEHYVAAPRRMLGAPLRQRRVRPLQELCRQ
105	TFSSKSEYQLVVNAVRKLQESGFYWSAVTGGEANLLLSAEPAGTFLIRDSSDQRHFFTLSVKTQSGTKNLRIQCEGGSFSLQSDPRSTQPVPRFDCVLKLVHHYMPPPGAPSFPSPPTEPSSEVPEQPSAQPLP
106	VHTQIDYIHCLVPDLLQITGNPCYWGVMDRYEAEALLEGKPEGTFLLRDSAQEDYLFSVSFRRYNRSLHARIEQWNHNFSFDAHDPCVFHSSTVTGLLEHYKDPSSCMFFEPLLTISLNRTFPFSLQ
107	QHLQCPLYRPDSSSFAASLRELEKCGWYWGPMNWEDAEMKLKGKPDGSFLVRDSSDPRYILSLSFRSQGITHHTRMEHYRGTFSLWCHPKFEDRCQSVVEFIKRAIMHSKNGKFLYFLRSRVPGLPPTPVQLL
108	SAGLVPITHVAKASPETLSDQPWYFSGVSRTQAQQLLLSPPNEPGAFLIRPSESSLGGYSLSVRAQAKVCHYRVSMAADGSLYLQKGRLFPGLEELLTYYKANWKLIQNPLLQPCMPQKAPRQDVW
109	GHLYMMSEVLAKEEARRALETPSCFLKVSRLEAQLLLERYPECGNLLLRPSGDGADGVSVTTRQMHNGTHVVRHYKVKREGPKYVIDVEQPFSCTSLDAVVNYFVSHTKKALVPFLLDEDYEKVLGYVEA
110	KLPFWTWLDKILELVHDHLKDLWNDGRIMGFVSRSQERRLLKKTMSGTFLLRFSESSEGGITCSWVEHQDDDKVLIYSVQPYTKEVLQSLPLTEIIRHYQLLTEELHIISFTVKYTYQGLKQELK
111	WTWLEAILDLIKKHILPLWIDGYVMGFVSKEKERLLLKDKMPGTFLLRFSESHLGGITFTWVDHSESGEVRFHSVEPYNKGRLSALPFADILRDYKVIMAENIPENPLKYLYPDIPKDKAFGKHYSSQPCEVSRPTE
112	NYTFWQWFDGVMEVLKKHHKPHWNDGAILGFVNKQQAHDLLINKPDGTFLLRFSDSEIGGITIAWKFDSPERNLWNLKPFTTRDFSIRSLADRLGDLSYLIYVFPDRPKDEVFSKYYTPVLAKA
113	QEEDMKRKQQRTTYIKRVIAHPSFHNINFKQAEKMMETMDQGDVIIRPSSKGENHLTVTWKVSDGIYQHVDVREEGKENAFSLGATLWINSEEFEDLDEIVARYVQPMASFARDLLNHKYYQDCSGGDRK
114	NEGYIPSNYVTGKKSNNLDQYEWYCRNMNRSKAEQLLRSEDKEGGFMVRDSSQPGLYTVSLYTKFGGEGSSGFRHYHIKETTTSPKKYYLAEKHAFGSIPEIIEYHKHNAAGLVTRLRYPVSVKGKNAPTTA
115	SMPDNSPETRAKVKFVQDTSKYWYKPEISREQAIALLKDQEPGAFIIRDSHSFRGAYGLAMKVSSPPPTIMQQNKKGDMTHELVRHFLIETGPRGVKLKGCPNEPNFGSLSALVYQHSIIPLALPCKLVIPNRDPTDESKDSS
116	PLPDSPGDKLVIVKFVQDTSKFWYKADISREQAIAMLKDKEPGSFIVRDSHSFRGAYGLAMKVATPPPSVLQLNKKAGDLANELVRHFLIECTPKGVRLKGCSNEPYFGSLTALVCQHSITPLALPCKLLIPERDPLEEIAESS
117	CPEGPARDMQPTMKFVMDTSKYWFKPNITREQAIELLRKEEPGAFVIRDSSSYRGSFGLALKVQEVPASAQNRPGEDSNDLIRHFLIESSAKGVHLKGADEEPYFGSLSAFVCQHSIMALALPCKLTIPQRELGGADGASD
118	HYLCHEVAPPRLVMSIRDGIHGPLLEPFVQAKLRPEDGLYLIHWSTSHPYRLILTVAQRSQAPDGMQSLRLRKFPIEQQDGAFVLEGWGRFPSVRELGAALQGCLLRAGDDCFSLRRCCLPQPGETS
119	FPSDAVKPCPCVPKPVDYSCQPWYAGAMERLQAETELINRVNSTYLVRHRTKESGEYAISIKYNNEAKHIKILTRDGFFHIAENRKFKSLMELVEYYKHHSLKEGFRTLDTTLQFPYKEPEHS
120	TGKNGYIPSNYVAPADSIQAEEWYFGKMGRKDAERLLLNPGNQRGIFLVRESETTKGAYSLSIRDWDEIRGDNVKHYKIRKLDNGGYYITTRAQFDTLQKLVKHYTEHADGLCHKLTTVCPTVKPQTQG
\.


--
-- Data for Name: species; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.species (id, latin_name, common_name) FROM stdin;
4	Homo sapiens	Human
\.


--
-- Data for Name: structure; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.structure (id, pdb_code, publication_date, resolution, publication_id, structure_type_id) FROM stdin;
\.


--
-- Data for Name: structure_domain; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.structure_domain (id, chain_id, domain_id, pdbdata_id) FROM stdin;
\.


--
-- Data for Name: structure_type; Type: TABLE DATA; Schema: public; Owner: SH2
--

COPY public.structure_type (id, slug, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 100, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: chain_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.chain_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 25, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 27, true);


--
-- Name: pdbdata_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.pdbdata_id_seq', 1, false);


--
-- Name: protein_conformation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.protein_conformation_id_seq', 1, false);


--
-- Name: protein_domain_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.protein_domain_id_seq', 418, true);


--
-- Name: protein_domaintype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.protein_domaintype_id_seq', 2, true);


--
-- Name: protein_family_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.protein_family_id_seq', 60, true);


--
-- Name: protein_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.protein_id_seq', 381, true);


--
-- Name: protein_isoform_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.protein_isoform_id_seq', 381, true);


--
-- Name: protein_segment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.protein_segment_id_seq', 1, false);


--
-- Name: protein_state_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.protein_state_id_seq', 1, false);


--
-- Name: publication_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.publication_id_seq', 1, false);


--
-- Name: residue_generic_number_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.residue_generic_number_id_seq', 1, false);


--
-- Name: residue_generic_numbering_scheme_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.residue_generic_numbering_scheme_id_seq', 1, false);


--
-- Name: residue_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.residue_id_seq', 1, false);


--
-- Name: sequence_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.sequence_id_seq', 120, true);


--
-- Name: species_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.species_id_seq', 4, true);


--
-- Name: structure_domain_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.structure_domain_id_seq', 1, false);


--
-- Name: structure_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.structure_id_seq', 1, false);


--
-- Name: structure_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: SH2
--

SELECT pg_catalog.setval('public.structure_type_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: chain chain_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.chain
    ADD CONSTRAINT chain_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: pdbdata pdbdata_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.pdbdata
    ADD CONSTRAINT pdbdata_pkey PRIMARY KEY (id);


--
-- Name: protein_conformation protein_conformation_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_conformation
    ADD CONSTRAINT protein_conformation_pkey PRIMARY KEY (id);


--
-- Name: protein_domain protein_domain_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_domain
    ADD CONSTRAINT protein_domain_pkey PRIMARY KEY (id);


--
-- Name: protein_domaintype protein_domaintype_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_domaintype
    ADD CONSTRAINT protein_domaintype_pkey PRIMARY KEY (id);


--
-- Name: protein_domaintype protein_domaintype_slug_key; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_domaintype
    ADD CONSTRAINT protein_domaintype_slug_key UNIQUE (slug);


--
-- Name: protein protein_entry_name_key; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein
    ADD CONSTRAINT protein_entry_name_key UNIQUE (entry_name);


--
-- Name: protein_family protein_family_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_family
    ADD CONSTRAINT protein_family_pkey PRIMARY KEY (id);


--
-- Name: protein_family protein_family_slug_key; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_family
    ADD CONSTRAINT protein_family_slug_key UNIQUE (slug);


--
-- Name: protein_isoform protein_isoform_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_isoform
    ADD CONSTRAINT protein_isoform_pkey PRIMARY KEY (id);


--
-- Name: protein protein_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein
    ADD CONSTRAINT protein_pkey PRIMARY KEY (id);


--
-- Name: protein_segment protein_segment_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_segment
    ADD CONSTRAINT protein_segment_pkey PRIMARY KEY (id);


--
-- Name: protein_segment protein_segment_slug_proteinfamily_129382b2_uniq; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_segment
    ADD CONSTRAINT protein_segment_slug_proteinfamily_129382b2_uniq UNIQUE (slug, proteinfamily);


--
-- Name: protein_state protein_state_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_state
    ADD CONSTRAINT protein_state_pkey PRIMARY KEY (id);


--
-- Name: protein_state protein_state_slug_key; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_state
    ADD CONSTRAINT protein_state_slug_key UNIQUE (slug);


--
-- Name: publication publication_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.publication
    ADD CONSTRAINT publication_pkey PRIMARY KEY (id);


--
-- Name: residue_generic_number residue_generic_number_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.residue_generic_number
    ADD CONSTRAINT residue_generic_number_pkey PRIMARY KEY (id);


--
-- Name: residue_generic_number residue_generic_number_scheme_id_label_63f09527_uniq; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.residue_generic_number
    ADD CONSTRAINT residue_generic_number_scheme_id_label_63f09527_uniq UNIQUE (scheme_id, label);


--
-- Name: residue_generic_numbering_scheme residue_generic_numbering_scheme_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.residue_generic_numbering_scheme
    ADD CONSTRAINT residue_generic_numbering_scheme_pkey PRIMARY KEY (id);


--
-- Name: residue residue_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.residue
    ADD CONSTRAINT residue_pkey PRIMARY KEY (id);


--
-- Name: sequence sequence_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.sequence
    ADD CONSTRAINT sequence_pkey PRIMARY KEY (id);


--
-- Name: species species_latin_name_key; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.species
    ADD CONSTRAINT species_latin_name_key UNIQUE (latin_name);


--
-- Name: species species_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.species
    ADD CONSTRAINT species_pkey PRIMARY KEY (id);


--
-- Name: structure_domain structure_domain_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.structure_domain
    ADD CONSTRAINT structure_domain_pkey PRIMARY KEY (id);


--
-- Name: structure structure_pdb_code_key; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.structure
    ADD CONSTRAINT structure_pdb_code_key UNIQUE (pdb_code);


--
-- Name: structure structure_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.structure
    ADD CONSTRAINT structure_pkey PRIMARY KEY (id);


--
-- Name: structure_type structure_type_pkey; Type: CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.structure_type
    ADD CONSTRAINT structure_type_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: chain_structure_id_f6927cb9; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX chain_structure_id_f6927cb9 ON public.chain USING btree (structure_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: protein_accession_704dea01; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_accession_704dea01 ON public.protein USING btree (accession);


--
-- Name: protein_accession_704dea01_like; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_accession_704dea01_like ON public.protein USING btree (accession varchar_pattern_ops);


--
-- Name: protein_conformation_domain_id_b160d30e; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_conformation_domain_id_b160d30e ON public.protein_conformation USING btree (domain_id);


--
-- Name: protein_conformation_state_id_1266255d; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_conformation_state_id_1266255d ON public.protein_conformation USING btree (state_id);


--
-- Name: protein_domain_domain_type_id_84081226; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_domain_domain_type_id_84081226 ON public.protein_domain USING btree (domain_type_id);


--
-- Name: protein_domain_isoform_id_978b098e; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_domain_isoform_id_978b098e ON public.protein_domain USING btree (isoform_id);


--
-- Name: protein_domain_parent_id_9bbc169d; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_domain_parent_id_9bbc169d ON public.protein_domain USING btree (parent_id);


--
-- Name: protein_domain_sequence_id_a0781623; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_domain_sequence_id_a0781623 ON public.protein_domain USING btree (sequence_id);


--
-- Name: protein_domaintype_slug_49c61d8d_like; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_domaintype_slug_49c61d8d_like ON public.protein_domaintype USING btree (slug varchar_pattern_ops);


--
-- Name: protein_entry_name_522ae454_like; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_entry_name_522ae454_like ON public.protein USING btree (entry_name varchar_pattern_ops);


--
-- Name: protein_family_id_00ab64d8; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_family_id_00ab64d8 ON public.protein USING btree (family_id);


--
-- Name: protein_family_parent_id_5ba26a78; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_family_parent_id_5ba26a78 ON public.protein_family USING btree (parent_id);


--
-- Name: protein_family_slug_a9a51f0e_like; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_family_slug_a9a51f0e_like ON public.protein_family USING btree (slug varchar_pattern_ops);


--
-- Name: protein_isoform_accession_80aeb928; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_isoform_accession_80aeb928 ON public.protein_isoform USING btree (accession);


--
-- Name: protein_isoform_accession_80aeb928_like; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_isoform_accession_80aeb928_like ON public.protein_isoform USING btree (accession varchar_pattern_ops);


--
-- Name: protein_isoform_protein_id_0993ff21; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_isoform_protein_id_0993ff21 ON public.protein_isoform USING btree (protein_id);


--
-- Name: protein_parent_id_8094e99d; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_parent_id_8094e99d ON public.protein USING btree (parent_id);


--
-- Name: protein_segment_slug_3c2359f1; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_segment_slug_3c2359f1 ON public.protein_segment USING btree (slug);


--
-- Name: protein_segment_slug_3c2359f1_like; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_segment_slug_3c2359f1_like ON public.protein_segment USING btree (slug varchar_pattern_ops);


--
-- Name: protein_species_id_4d4ff6de; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_species_id_4d4ff6de ON public.protein USING btree (species_id);


--
-- Name: protein_state_slug_e86cb3df_like; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX protein_state_slug_e86cb3df_like ON public.protein_state USING btree (slug varchar_pattern_ops);


--
-- Name: residue_domain_id_e2ecab07; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX residue_domain_id_e2ecab07 ON public.residue USING btree (domain_id);


--
-- Name: residue_generic_number_id_bfa88971; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX residue_generic_number_id_bfa88971 ON public.residue USING btree (generic_number_id);


--
-- Name: residue_generic_number_label_767482b5; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX residue_generic_number_label_767482b5 ON public.residue_generic_number USING btree (label);


--
-- Name: residue_generic_number_label_767482b5_like; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX residue_generic_number_label_767482b5_like ON public.residue_generic_number USING btree (label varchar_pattern_ops);


--
-- Name: residue_generic_number_protein_segment_id_c66a62a0; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX residue_generic_number_protein_segment_id_c66a62a0 ON public.residue_generic_number USING btree (protein_segment_id);


--
-- Name: residue_generic_number_scheme_id_deacdcbf; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX residue_generic_number_scheme_id_deacdcbf ON public.residue_generic_number USING btree (scheme_id);


--
-- Name: residue_generic_numbering_scheme_parent_id_142b9ccc; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX residue_generic_numbering_scheme_parent_id_142b9ccc ON public.residue_generic_numbering_scheme USING btree (parent_id);


--
-- Name: residue_generic_numbering_scheme_slug_2d0226b1; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX residue_generic_numbering_scheme_slug_2d0226b1 ON public.residue_generic_numbering_scheme USING btree (slug);


--
-- Name: residue_generic_numbering_scheme_slug_2d0226b1_like; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX residue_generic_numbering_scheme_slug_2d0226b1_like ON public.residue_generic_numbering_scheme USING btree (slug varchar_pattern_ops);


--
-- Name: residue_protein_segment_id_817e7495; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX residue_protein_segment_id_817e7495 ON public.residue USING btree (protein_segment_id);


--
-- Name: species_latin_name_c88032b5_like; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX species_latin_name_c88032b5_like ON public.species USING btree (latin_name varchar_pattern_ops);


--
-- Name: structure_domain_chain_id_97cc0374; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX structure_domain_chain_id_97cc0374 ON public.structure_domain USING btree (chain_id);


--
-- Name: structure_domain_domain_id_393e8b79; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX structure_domain_domain_id_393e8b79 ON public.structure_domain USING btree (domain_id);


--
-- Name: structure_domain_pdbdata_id_03fc800b; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX structure_domain_pdbdata_id_03fc800b ON public.structure_domain USING btree (pdbdata_id);


--
-- Name: structure_pdb_code_49b0d327_like; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX structure_pdb_code_49b0d327_like ON public.structure USING btree (pdb_code varchar_pattern_ops);


--
-- Name: structure_publication_id_dbe3080f; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX structure_publication_id_dbe3080f ON public.structure USING btree (publication_id);


--
-- Name: structure_structure_type_id_02d1e690; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX structure_structure_type_id_02d1e690 ON public.structure USING btree (structure_type_id);


--
-- Name: structure_type_slug_46480f7a; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX structure_type_slug_46480f7a ON public.structure_type USING btree (slug);


--
-- Name: structure_type_slug_46480f7a_like; Type: INDEX; Schema: public; Owner: SH2
--

CREATE INDEX structure_type_slug_46480f7a_like ON public.structure_type USING btree (slug varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: chain chain_structure_id_f6927cb9_fk_structure_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.chain
    ADD CONSTRAINT chain_structure_id_f6927cb9_fk_structure_id FOREIGN KEY (structure_id) REFERENCES public.structure(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: protein_conformation protein_conformation_domain_id_b160d30e_fk_protein_domain_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_conformation
    ADD CONSTRAINT protein_conformation_domain_id_b160d30e_fk_protein_domain_id FOREIGN KEY (domain_id) REFERENCES public.protein_domain(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: protein_conformation protein_conformation_state_id_1266255d_fk_protein_state_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_conformation
    ADD CONSTRAINT protein_conformation_state_id_1266255d_fk_protein_state_id FOREIGN KEY (state_id) REFERENCES public.protein_state(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: protein_domain protein_domain_domain_type_id_84081226_fk_protein_domaintype_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_domain
    ADD CONSTRAINT protein_domain_domain_type_id_84081226_fk_protein_domaintype_id FOREIGN KEY (domain_type_id) REFERENCES public.protein_domaintype(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: protein_domain protein_domain_isoform_id_978b098e_fk_protein_isoform_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_domain
    ADD CONSTRAINT protein_domain_isoform_id_978b098e_fk_protein_isoform_id FOREIGN KEY (isoform_id) REFERENCES public.protein_isoform(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: protein_domain protein_domain_parent_id_9bbc169d_fk_protein_domain_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_domain
    ADD CONSTRAINT protein_domain_parent_id_9bbc169d_fk_protein_domain_id FOREIGN KEY (parent_id) REFERENCES public.protein_domain(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: protein_domain protein_domain_sequence_id_a0781623_fk_sequence_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_domain
    ADD CONSTRAINT protein_domain_sequence_id_a0781623_fk_sequence_id FOREIGN KEY (sequence_id) REFERENCES public.sequence(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: protein protein_family_id_00ab64d8_fk_protein_family_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein
    ADD CONSTRAINT protein_family_id_00ab64d8_fk_protein_family_id FOREIGN KEY (family_id) REFERENCES public.protein_family(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: protein_family protein_family_parent_id_5ba26a78_fk_protein_family_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_family
    ADD CONSTRAINT protein_family_parent_id_5ba26a78_fk_protein_family_id FOREIGN KEY (parent_id) REFERENCES public.protein_family(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: protein_isoform protein_isoform_protein_id_0993ff21_fk_protein_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein_isoform
    ADD CONSTRAINT protein_isoform_protein_id_0993ff21_fk_protein_id FOREIGN KEY (protein_id) REFERENCES public.protein(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: protein protein_parent_id_8094e99d_fk_protein_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein
    ADD CONSTRAINT protein_parent_id_8094e99d_fk_protein_id FOREIGN KEY (parent_id) REFERENCES public.protein(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: protein protein_species_id_4d4ff6de_fk_species_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.protein
    ADD CONSTRAINT protein_species_id_4d4ff6de_fk_species_id FOREIGN KEY (species_id) REFERENCES public.species(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: residue residue_domain_id_e2ecab07_fk_protein_domain_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.residue
    ADD CONSTRAINT residue_domain_id_e2ecab07_fk_protein_domain_id FOREIGN KEY (domain_id) REFERENCES public.protein_domain(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: residue_generic_numbering_scheme residue_generic_numb_parent_id_142b9ccc_fk_residue_g; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.residue_generic_numbering_scheme
    ADD CONSTRAINT residue_generic_numb_parent_id_142b9ccc_fk_residue_g FOREIGN KEY (parent_id) REFERENCES public.residue_generic_numbering_scheme(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: residue_generic_number residue_generic_numb_protein_segment_id_c66a62a0_fk_protein_s; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.residue_generic_number
    ADD CONSTRAINT residue_generic_numb_protein_segment_id_c66a62a0_fk_protein_s FOREIGN KEY (protein_segment_id) REFERENCES public.protein_segment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: residue_generic_number residue_generic_numb_scheme_id_deacdcbf_fk_residue_g; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.residue_generic_number
    ADD CONSTRAINT residue_generic_numb_scheme_id_deacdcbf_fk_residue_g FOREIGN KEY (scheme_id) REFERENCES public.residue_generic_numbering_scheme(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: residue residue_generic_number_id_bfa88971_fk_residue_generic_number_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.residue
    ADD CONSTRAINT residue_generic_number_id_bfa88971_fk_residue_generic_number_id FOREIGN KEY (generic_number_id) REFERENCES public.residue_generic_number(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: residue residue_protein_segment_id_817e7495_fk_protein_segment_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.residue
    ADD CONSTRAINT residue_protein_segment_id_817e7495_fk_protein_segment_id FOREIGN KEY (protein_segment_id) REFERENCES public.protein_segment(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: structure_domain structure_domain_chain_id_97cc0374_fk_chain_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.structure_domain
    ADD CONSTRAINT structure_domain_chain_id_97cc0374_fk_chain_id FOREIGN KEY (chain_id) REFERENCES public.chain(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: structure_domain structure_domain_domain_id_393e8b79_fk_protein_domain_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.structure_domain
    ADD CONSTRAINT structure_domain_domain_id_393e8b79_fk_protein_domain_id FOREIGN KEY (domain_id) REFERENCES public.protein_domain(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: structure_domain structure_domain_pdbdata_id_03fc800b_fk_pdbdata_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.structure_domain
    ADD CONSTRAINT structure_domain_pdbdata_id_03fc800b_fk_pdbdata_id FOREIGN KEY (pdbdata_id) REFERENCES public.pdbdata(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: structure structure_publication_id_dbe3080f_fk_publication_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.structure
    ADD CONSTRAINT structure_publication_id_dbe3080f_fk_publication_id FOREIGN KEY (publication_id) REFERENCES public.publication(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: structure structure_structure_type_id_02d1e690_fk_structure_type_id; Type: FK CONSTRAINT; Schema: public; Owner: SH2
--

ALTER TABLE ONLY public.structure
    ADD CONSTRAINT structure_structure_type_id_02d1e690_fk_structure_type_id FOREIGN KEY (structure_type_id) REFERENCES public.structure_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

