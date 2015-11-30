// -*- C++ -*-
//
// Package:    PhysVal/MuonPtFilter
// Class:      MuonPtFilter
// 
/**\class MuonPtFilter MuonPtFilter.cc PhysVal/MuonPtFilter/plugins/MuonPtFilter.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Aysen Tatarinov
//         Created:  Tue, 24 Nov 2015 02:44:24 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"

//
// class declaration
//

class MuonPtFilter : public edm::EDFilter {
   public:
      explicit MuonPtFilter(const edm::ParameterSet&);
      ~MuonPtFilter();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() override;
      virtual bool filter(edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
      
      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
MuonPtFilter::MuonPtFilter(const edm::ParameterSet& iConfig)
{
   //now do what ever initialization is needed

}


MuonPtFilter::~MuonPtFilter()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
MuonPtFilter::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    edm::Handle<reco::MuonCollection> recoMuonCollection;
    iEvent.getByLabel("muons", recoMuonCollection);
    
    edm::Handle<reco::BeamSpot> beamspot;
    iEvent.getByLabel("offlineBeamSpot", beamspot);

      if ( recoMuonCollection.isValid() ) {
          for (reco::MuonCollection::const_iterator muon = recoMuonCollection->begin();  muon != recoMuonCollection->end();  ++muon) {
              if ( muon->isGlobalMuon() && muon->isStandAloneMuon() ) {
                  if (    muon->globalTrack()->normalizedChi2()   < 10
                       && muon->innerTrack()->numberOfValidHits() > 10
                       && muon->numberOfMatchedStations() > 1
                       && fabs( muon->innerTrack()->dxy( beamspot->position() ) ) < 0.2 && muon->innerTrack()->pt() > 60.0) {
                        return true;
                  }
              }
          }
      }

    return false;
}

// ------------ method called once each job just before starting event loop  ------------
void 
MuonPtFilter::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
MuonPtFilter::endJob() {
}

// ------------ method called when starting to processes a run  ------------
/*
void
MuonPtFilter::beginRun(edm::Run const&, edm::EventSetup const&)
{ 
}
*/
 
// ------------ method called when ending the processing of a run  ------------
/*
void
MuonPtFilter::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when starting to processes a luminosity block  ------------
/*
void
MuonPtFilter::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
MuonPtFilter::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
MuonPtFilter::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(MuonPtFilter);
