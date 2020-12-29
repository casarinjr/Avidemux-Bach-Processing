# BATCH CONVERT all the files with listed extensions to MP4 HEVC(AQ26)/ACC with no filters.
#
#IMPUT AS MANY EXTENSIONS AS YOU WANT IN THE ext=() LIST:
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
ext=("mp4","mkv","avi","wmv")
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#
gui=Gui()
adm=Avidemux()
inputFolder=gui.dirSelect("Select the source folder")
print("Input folder: " + inputFolder)
outputFolder=gui.dirSelect("Select the output folder")
print("Output folder: " + outputFolder)

#
def convert(filein):
    filename = basename(filein)
    dir = dirname(filein)
    if(0 == adm.loadVideo(filein)):
        gui.displayError("Oops","Cannot load "+filein)
    else:
        # SETTINGS: MP4 H265(AQ26)/ACC
        adm.videoCodec("x265", "useAdvancedConfiguration=True", "general.params=AQ=26", "general.poolThreads=99", "general.frameThreads=0", "general.preset=ultrafast", "general.tuning=none", "general.profile=main", "level=-1", "vui.sar_height=1"
        , "vui.sar_width=1", "MaxRefFrames=3", "MinIdr=25", "MaxIdr=250", "i_scenecut_threshold=40", "MaxBFrame=3", "i_bframe_adaptive=1", "i_bframe_bias=0", "i_bframe_pyramid=2", "b_deblocking_filter=True", "b_open_gop=True"
        , "interlaced_mode=0", "constrained_intra=False", "lookahead=40", "weighted_pred=2", "weighted_bipred=True", "cb_chroma_offset=0", "cr_chroma_offset=0", "me_method=3", "me_range=16", "subpel_refine=5"
        , "trellis=1", "psy_rd=1.000000", "fast_pskip=True", "dct_decimate=True", "noise_reduction=0", "noise_reduction_intra=0", "noise_reduction_inter=0", "strong_intra_smoothing=True", "ratecontrol.rc_method=0"
        , "ratecontrol.qp_constant=0", "ratecontrol.qp_step=4", "ratecontrol.bitrate=0", "ratecontrol.rate_tolerance=1.000000", "ratecontrol.vbv_max_bitrate=0", "ratecontrol.vbv_buffer_size=0", "ratecontrol.vbv_buffer_init=1"
        , "ratecontrol.ip_factor=1.400000", "ratecontrol.pb_factor=1.300000", "ratecontrol.aq_mode=2", "ratecontrol.aq_strength=1.000000", "ratecontrol.cu_tree=True", "ratecontrol.strict_cbr=False")
        adm.audioCodec(0, "FDK_AAC");
        adm.setContainer("MP4", "muxerType=0", "optimize=1", "forceAspectRatio=False", "aspectRatio=1", "rotation=0", "clockfreq=0")
        # FILTERS:[here you can add as many filters as you want]

        # SAVING
        adm.save(outputFolder + "/" + filename + ".converted.mp4")
        print("File done")
#
# Scanning and processing files in inputFolder by extension (ex):
def work(ex):
    list=get_folder_content(inputFolder,ex)
    if list is not None:
        print(list)
        for i in list:
          print(i)
          convert(i)
        print("Extension " + str(ex) + " done!")

#  work each extension in the list (ext):
for ex in ext:
    work(ex)

# THE END!
print("ALL DONE!")
gui.displayInfo("Task info:","BATCH PROCESSING COMPLETED!")
