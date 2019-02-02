CREATE TABLE public.reviewed
(
    id serial,
    accepted boolean,
    "userId" character varying(255)[],
    PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
);

ALTER TABLE public.reviewed
    OWNER to bbd;

ALTER TABLE public.notes DROP COLUMN reviewed;

ALTER TABLE public.notes DROP COLUMN "time";

ALTER TABLE public.notes DROP COLUMN user_id;

ALTER TABLE public.notes
    ADD COLUMN reviewed integer;

ALTER TABLE public.tags ADD COLUMN notes_id integer;

ALTER TABLE public.tags
    ADD CONSTRAINT "FK_notes_ids" FOREIGN KEY (notes_id)
    REFERENCES public.notes (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE CASCADE;
CREATE INDEX "fki_FK_notes_ids"
    ON public.tags(notes_id);