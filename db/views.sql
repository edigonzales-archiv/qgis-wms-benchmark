CREATE OR REPLACE VIEW av_avdpool_next.v_liegenschaften_grundstueckpos AS
SELECT p.*, g.nummer
FROM av_avdpool_next.liegenschaften_grundstueck as g, av_avdpool_next.liegenschaften_grundstueckpos as p
WHERE g.t_id = p.grundstueckpos_von;

ALTER TABLE av_avdpool_next.v_liegenschaften_grundstueckpos
  OWNER TO stefan;