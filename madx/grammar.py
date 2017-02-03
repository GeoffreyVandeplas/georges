"""A dictionnary for the translation of the MAD-X grammar."""

madx_syntax = {  # Do not forget the trailing ';' for each command!
    'beam': "BEAM, PARTICLE={{{{PARTICLE}}}}, PC={{{{PC}}}};",
    'show_beam': "SHOW, BEAM;",
    'call_file': "CALL, FILE='{}';",
    'use_sequence': "USE, SEQUENCE={};",
    'save_beta': "SAVEBETA, LABEL={}, PLACE={};",
    'makethin': "MAKETHIN, sequence={}, style={};",
    'twiss_beamline': "TWISS,"
                      "BETX={{{{ BETAX }}}},"
                      "ALFX= {{{{ ALPHAX}}}},"
                      "MUX=0.0,"
                      "BETY={{{{ BETAY }}}},"
                      "ALFY={{{{ ALPHAY }}}},"
                      "MUY=0.0,"
                      "DX=0.0,"
                      "DPX=0.0,"
                      "DY=0.0,"
                      "DPY=0.0,"
                      "X=0.0,"
                      "PX=0.0,"
                      "Y=0.0,"
                      "PY= 0.0,"
                      "T=0.0,"
                      "PT=0.0,"
                      "DELTAP={{{{ DELTAP }}}},"
                      "FILE={}"
                      "{};",  # Note the optional args
    'track_beamline': "TRACK,"
                      "DELTAP={{{{ DELTAP }}}},"
                      "ONEPASS=true,"
                      "APERTURE=true,"
                      "DUMP=true,"
                      "ONETABLE=true,"
                      "FILE=tracking.outx;",
    'ptc_twiss_beamline': "PTC_TWISS,ICASE=6,"
                          "DELTAP={{{{ DELTAP }}}},"
                          "FILE={},"
                          "BETX={{{{ BETAX }}}},"
                          "ALFX={{{{ ALPHAX }}}},"
                          "MUX=0.0,"
                          "BETY={{{{ BETAY }}}},"
                          "ALFY={{{{ ALPHAY }}}},"
                          "MUY=0.0,"
                          "DX=0.0,"
                          "DPX=0.0,"
                          "DY=0.0,"
                          "DPY=0.0,"
                          "X=0.0,"
                          "PX=0.0,"
                          "Y=0.0,"
                          "PY=0.0,"
                          "T=0.0,"
                          "BETZ=1.0,"
                          "ALFZ=0.0,"
                          "MUZ=0.0,"
                          "PT=0.0,"
                          "SLICE_MAGNETS=true;",
    'run_track_beamline': "RUN, TURNS=1, MAXAPER=0.1,1.0,0.1,0.1,100.0,10.0;",  # Beamline so OK to hardcode TURNS=1
    'start_particle': "START, X={}, PX={}, Y={}, PY={}, T=0.0, PT={};",
    'observe': "OBSERVE, PLACE={};",
    'end_track': 'ENDTRACK;',
    'stop': "STOP;",
    'rbarc': "OPTION, RBARC=false;",
    'select_columns': "SELECT, FLAG={}, COLUMN={};",
    'eager_variable': "{} = {{{{ {} }}}};",  # Oops
    'lazy_variable': "{} := {{{{ {} }}}};",  # Oops
    'ptc_create_universe': "PTC_CREATE_UNIVERSE;",
    'ptc_create_layout': "PTC_CREATE_LAYOUT, TIME={}, MODEL={}, METHOD={}, NST={}, EXACT={};",
    'ptc_align': "PTC_ALIGN;",
    'ptc_end': "PTC_END;",
    'ptc_observe': "PTC_OBSERVE, PLACE={};",
    'ptc_start': "PTC_START, X={}, PX={}, Y={}, PY={}, T=0.0, PT={};",
    'ptc_track': "PTC_TRACK, ICASE={},"
                 "DELTAP={},"
                 "CLOSED_ORBIT={},"
                 "ELEMENT_BY_ELEMENT={},"
                 "TURNS={},"
                 "DUMP={},"
                 "ONETABLE={},"
                 "FILE={},"
                 "EXTENSION={};",
    'ptc_track_end': "PTC_TRACK_END;"
}