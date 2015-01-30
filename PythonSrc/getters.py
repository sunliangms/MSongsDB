"""
This file is the collection of getter functions to get fields from HDF5 song file.
All function names are self-explained.
"""

import tables

def openH5InRead(fInput):
    """
    Open an existing h5 file in  the read mode.
    """
    return tables.openFile(fInput, mode='r')

def getSongNum(h5Obj):
    return h5Obj.root.metadata.songs.nrows

def getArtistFamiliarity(h5Obj,sID=0):
    return h5Obj.root.metadata.songs.cols.artist_familiarity[sID]

def getArtistHotttnesss(h5Obj,sID=0):
    return h5Obj.root.metadata.songs.cols.artist_hotttnesss[sID]

def getArtistId(h5Obj,sID=0):
    return h5Obj.root.metadata.songs.cols.artist_id[sID]

def getArtistMbid(h5Obj,sID=0):
    return h5Obj.root.metadata.songs.cols.artist_mbid[sID]

def getArtistPlaymeid(h5Obj,sID=0):
    return h5Obj.root.metadata.songs.cols.artist_playmeid[sID]

def getArtist7digitalid(h5Obj,sID=0):
    return h5Obj.root.metadata.songs.cols.artist_7digitalid[sID]

def getArtistLatitude(h5Obj,sID=0):
    return h5Obj.root.metadata.songs.cols.artist_latitude[sID]

def getArtistLongitude(h5Obj,sID=0):
    return h5Obj.root.metadata.songs.cols.artist_longitude[sID]

def getArtistLocation(h5Obj,sID=0):
    return h5Obj.root.metadata.songs.cols.artist_location[sID]

def getArtistName(h5Obj,sID=0):
    return h5Obj.root.metadata.songs.cols.artist_name[sID]

def getRelease(h5Obj,sID=0):
    return h5Obj.root.metadata.songs.cols.release[sID]

def getRelease7digitalid(h5Obj,sID=0):
    return h5Obj.root.metadata.songs.cols.release_7digitalid[sID]

def getSongId(h5Obj,sID=0):
    return h5Obj.root.metadata.songs.cols.song_id[sID]

def getSongHotttnesss(h5Obj,sID=0):
    return h5Obj.root.metadata.songs.cols.song_hotttnesss[sID]

def getTitle(h5Obj,sID=0):
    return h5Obj.root.metadata.songs.cols.title[sID]

def getTrack7digitalid(h5Obj,sID=0):
    return h5Obj.root.metadata.songs.cols.track_7digitalid[sID]

def getSimilarArtists(h5Obj,sID=0):
    if h5Obj.root.metadata.songs.nrows-1 == sID:
        return h5Obj.root.metadata.similar_artists[h5Obj.root.metadata.songs.cols.idx_similar_artists[sID]:]
    else:
        return h5Obj.root.metadata.similar_artists[h5Obj.root.metadata.songs.cols.idx_similar_artists[sID]:
        h5Obj.root.metadata.songs.cols.idx_similar_artists[sID+1]]

def getArtistTerms(h5Obj,sID=0):
    if h5Obj.root.metadata.songs.nrows - 1 == sID:
        return h5Obj.root.metadata.artist_terms[h5Obj.root.metadata.songs.cols.idx_artist_terms[sID]:]
    else:
        return h5Obj.root.metadata.artist_terms[h5Obj.root.metadata.songs.cols.idx_artist_terms[sID]:
        h5Obj.root.metadata.songs.cols.idx_artist_terms[sID+1]]

def getArtistTermsFreq(h5Obj,sID=0):
    if h5Obj.root.metadata.songs.nrows-1 == sID:
        return h5Obj.root.metadata.artist_terms_freq[h5Obj.root.metadata.songs.cols.idx_artist_terms[sID]:]
    else:
        return h5Obj.root.metadata.artist_terms_freq[h5Obj.root.metadata.songs.cols.idx_artist_terms[sID]:
        h5Obj.root.metadata.songs.cols.idx_artist_terms[sID+1]]

def getArtistTermsWeight(h5Obj,sID=0):
    if h5Obj.root.metadata.songs.nrows-1 == sID:
        return h5Obj.root.metadata.artist_terms_weight[h5Obj.root.metadata.songs.cols.idx_artist_terms[sID]:]
    else:
        return h5Obj.root.metadata.artist_terms_weight[h5Obj.root.metadata.songs.cols.idx_artist_terms[sID]:
        h5Obj.root.metadata.songs.cols.idx_artist_terms[sID+1]]

def getAnalysisSampleRate(h5Obj,sID=0):
    return h5Obj.root.analysis.songs.cols.analysis_sample_rate[sID]

def getAudioMd5(h5Obj,sID=0):
    return h5Obj.root.analysis.songs.cols.audio_md5[sID]

def getDanceability(h5Obj,sID=0):
    return h5Obj.root.analysis.songs.cols.danceability[sID]

def getDuration(h5Obj,sID=0):
    return h5Obj.root.analysis.songs.cols.duration[sID]

def getEndOfFadeIn(h5Obj,sID=0):
    return h5Obj.root.analysis.songs.cols.end_of_fade_in[sID]

def getEnergy(h5Obj,sID=0):
    return h5Obj.root.analysis.songs.cols.energy[sID]

def getKey(h5Obj,sID=0):
    return h5Obj.root.analysis.songs.cols.key[sID]

def getKeyConfidence(h5Obj,sID=0):
    return h5Obj.root.analysis.songs.cols.key_confidence[sID]

def getLoudness(h5Obj,sID=0):
    return h5Obj.root.analysis.songs.cols.loudness[sID]

def getMode(h5Obj,sID=0):
    return h5Obj.root.analysis.songs.cols.mode[sID]

def getModeConfidence(h5Obj,sID=0):
    return h5Obj.root.analysis.songs.cols.mode_confidence[sID]

def getStartOfFadeOut(h5Obj,sID=0):
    return h5Obj.root.analysis.songs.cols.start_of_fade_out[sID]

def getTempo(h5Obj,sID=0):
    return h5Obj.root.analysis.songs.cols.tempo[sID]

def getTimeSignature(h5Obj,sID=0):
    return h5Obj.root.analysis.songs.cols.time_signature[sID]

def getTimeSignatureConfidence(h5Obj,sID=0):
    return h5Obj.root.analysis.songs.cols.time_signature_confidence[sID]

def getTrackId(h5Obj,sID=0):
    return h5Obj.root.analysis.songs.cols.track_id[sID]

def getSegmentsStart(h5Obj,sID=0):
    if h5Obj.root.analysis.songs.nrows-1 == sID:
        return h5Obj.root.analysis.segments_start[h5Obj.root.analysis.songs.cols.idx_segments_start[sID]:]
    else:
        return h5Obj.root.analysis.segments_start[h5Obj.root.analysis.songs.cols.idx_segments_start[sID]:
        h5Obj.root.analysis.songs.cols.idx_segments_start[sID+1]]

def getSegmentsConfidence(h5Obj,sID=0):
    if h5Obj.root.analysis.songs.nrows-1 == sID:
        return h5Obj.root.analysis.segments_confidence[h5Obj.root.analysis.songs.cols.idx_segments_confidence[sID]:]
    else:
        return h5Obj.root.analysis.segments_confidence[h5Obj.root.analysis.songs.cols.idx_segments_confidence[sID]:
        h5Obj.root.analysis.songs.cols.idx_segments_confidence[sID+1]]

def getSegmentsPitches(h5Obj,sID=0):
    if h5Obj.root.analysis.songs.nrows-1 == sID:
        return h5Obj.root.analysis.segments_pitches[h5Obj.root.analysis.songs.cols.idx_segments_pitches[sID]:,:]
    else:
        return h5Obj.root.analysis.segments_pitches[h5Obj.root.analysis.songs.cols.idx_segments_pitches[sID]:
        h5Obj.root.analysis.songs.cols.idx_segments_pitches[sID+1],:]

def getSegmentsTimbre(h5Obj,sID=0):
    if h5Obj.root.analysis.songs.nrows-1 == sID:
        return h5Obj.root.analysis.segments_timbre[h5Obj.root.analysis.songs.cols.idx_segments_timbre[sID]:,:]
    else:
        return h5Obj.root.analysis.segments_timbre[h5Obj.root.analysis.songs.cols.idx_segments_timbre[sID]:
        h5Obj.root.analysis.songs.cols.idx_segments_timbre[sID+1],:]

def getSegmentsLoudness_max(h5Obj,sID=0):
    if h5Obj.root.analysis.songs.nrows-1 == sID:
        return h5Obj.root.analysis.segments_loudness_max[h5Obj.root.analysis.songs.cols.idx_segments_loudness_max[sID]:]
    else:
        return h5Obj.root.analysis.segments_loudness_max[h5Obj.root.analysis.songs.cols.idx_segments_loudness_max[sID]:
        h5Obj.root.analysis.songs.cols.idx_segments_loudness_max[sID+1]]

def getSegmentsLoudnessMaxTime(h5Obj,sID=0):
    if h5Obj.root.analysis.songs.nrows-1 == sID:
        return h5Obj.root.analysis.segments_loudness_max_time[h5Obj.root.analysis.songs.cols.idx_segments_loudness_max_time[sID]:]
    else:
        return h5Obj.root.analysis.segments_loudness_max_time[h5Obj.root.analysis.songs.cols.idx_segments_loudness_max_time[sID]:
        h5Obj.root.analysis.songs.cols.idx_segments_loudness_max_time[sID+1]]

def getSegmentsLoudnessStart(h5Obj,sID=0):
    if h5Obj.root.analysis.songs.nrows-1 == sID:
        return h5Obj.root.analysis.segments_loudness_start[h5Obj.root.analysis.songs.cols.idx_segments_loudness_start[sID]:]
    else:
        return h5Obj.root.analysis.segments_loudness_start[h5Obj.root.analysis.songs.cols.idx_segments_loudness_start[sID]:
        h5Obj.root.analysis.songs.cols.idx_segments_loudness_start[sID+1]]

def getSectionsStart(h5Obj,sID=0):
    if h5Obj.root.analysis.songs.nrows-1 == sID:
        return h5Obj.root.analysis.sections_start[h5Obj.root.analysis.songs.cols.idx_sections_start[sID]:]
    else:
        return h5Obj.root.analysis.sections_start[h5Obj.root.analysis.songs.cols.idx_sections_start[sID]:
        h5Obj.root.analysis.songs.cols.idx_sections_start[sID+1]]

def getSectionsConfidence(h5Obj,sID=0):
    if h5Obj.root.analysis.songs.nrows-1 == sID:
        return h5Obj.root.analysis.sections_confidence[h5Obj.root.analysis.songs.cols.idx_sections_confidence[sID]:]
    else:
        return h5Obj.root.analysis.sections_confidence[h5Obj.root.analysis.songs.cols.idx_sections_confidence[sID]:
        h5Obj.root.analysis.songs.cols.idx_sections_confidence[sID+1]]

def getBeatsStart(h5Obj,sID=0):
    if h5Obj.root.analysis.songs.nrows-1 == sID:
        return h5Obj.root.analysis.beats_start[h5Obj.root.analysis.songs.cols.idx_beats_start[sID]:]
    else:
        return h5Obj.root.analysis.beats_start[h5Obj.root.analysis.songs.cols.idx_beats_start[sID]:
        h5Obj.root.analysis.songs.cols.idx_beats_start[sID+1]]

def getBeatsConfidence(h5Obj,sID=0):
    if h5Obj.root.analysis.songs.nrows-1 == sID:
        return h5Obj.root.analysis.beats_confidence[h5Obj.root.analysis.songs.cols.idx_beats_confidence[sID]:]
    else:
        return h5Obj.root.analysis.beats_confidence[h5Obj.root.analysis.songs.cols.idx_beats_confidence[sID]:
        h5Obj.root.analysis.songs.cols.idx_beats_confidence[sID+1]]

def getBarsStart(h5Obj,sID=0):
    if h5Obj.root.analysis.songs.nrows-1 == sID:
        return h5Obj.root.analysis.bars_start[h5Obj.root.analysis.songs.cols.idx_bars_start[sID]:]
    else:
        return h5Obj.root.analysis.bars_start[h5Obj.root.analysis.songs.cols.idx_bars_start[sID]:
        h5Obj.root.analysis.songs.cols.idx_bars_start[sID+1]]

def getBarsConfidence(h5Obj,sID=0):
    if h5Obj.root.analysis.songs.nrows-1 == sID:
        return h5Obj.root.analysis.bars_confidence[h5Obj.root.analysis.songs.cols.idx_bars_confidence[sID]:]
    else:
        return h5Obj.root.analysis.bars_confidence[h5Obj.root.analysis.songs.cols.idx_bars_confidence[sID]:
        h5Obj.root.analysis.songs.cols.idx_bars_confidence[sID+1]]

def getTatumsStart(h5Obj,sID=0):
    if h5Obj.root.analysis.songs.nrows-1 == sID:
        return h5Obj.root.analysis.tatums_start[h5Obj.root.analysis.songs.cols.idx_tatums_start[sID]:]
    else:
        return h5Obj.root.analysis.tatums_start[h5Obj.root.analysis.songs.cols.idx_tatums_start[sID]:
        h5Obj.root.analysis.songs.cols.idx_tatums_start[sID+1]]

def getTatumsConfidence(h5Obj,sID=0):
    if h5Obj.root.analysis.songs.nrows-1 == sID:
        return h5Obj.root.analysis.tatums_confidence[h5Obj.root.analysis.songs.cols.idx_tatums_confidence[sID]:]
    else:
        return h5Obj.root.analysis.tatums_confidence[h5Obj.root.analysis.songs.cols.idx_tatums_confidence[sID]:
        h5Obj.root.analysis.songs.cols.idx_tatums_confidence[sID+1]]

def getArtistMbtags(h5Obj,sID=0):
    if h5Obj.root.musicbrainz.songs.nrows-1 == sID:
        return h5Obj.root.musicbrainz.artist_mbtags[h5Obj.root.musicbrainz.songs.cols.idx_artist_mbtags[sID]:]
    else:
        return h5Obj.root.musicbrainz.artist_mbtags[h5Obj.root.metadata.songs.cols.idx_artist_mbtags[sID]:
        h5Obj.root.metadata.songs.cols.idx_artist_mbtags[sID+1]]

def getArtistMbtags_count(h5Obj,sID=0):
    if h5Obj.root.musicbrainz.songs.nrows-1 == sID:
        return h5Obj.root.musicbrainz.artist_mbtags_count[h5Obj.root.musicbrainz.songs.cols.idx_artist_mbtags[sID]:]
    else:
        return h5Obj.root.musicbrainz.artist_mbtags_count[h5Obj.root.metadata.songs.cols.idx_artist_mbtags[sID]:
        h5Obj.root.metadata.songs.cols.idx_artist_mbtags[sID+1]]

def getYear(h5Obj,sID=0):
    return h5Obj.root.musicbrainz.songs.cols.year[sID]
