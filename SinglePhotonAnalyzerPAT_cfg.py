
import FWCore.ParameterSet.Config as cms

process = cms.Process("SGAnalysis")

## MessageLogger
process.load("FWCore.MessageLogger.MessageLogger_cfi")

## Options and Output Report
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )

## Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:/tmp/ganzhur/PhotonJet_skim_pt30.root'
    )
)
## Maximal Number of Events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

## Geometry and Detector Conditions (needed for a few patTuple production steps)
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('STARTUP31X_V1::All')
process.load("Configuration.StandardSequences.MagneticField_cff")


# Input pat analyzer sequence
process.load("UserCode.SGAnalysis.SinglePhotonAnalyzer_cfi")

process.singlePhotonAnalyzer.IsMCData              = True
process.singlePhotonAnalyzer.FillMCNTuple          = True
process.singlePhotonAnalyzer.OutputFile            = 'test.root'

## Analyser path
process.p = cms.Path(process.singlePhotonAnalyzer)





