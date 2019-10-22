# Notes on Geolocation Processor


# Roles of Mirror Offset Variable

Variable `mirrorOffset` plalys an important role when



# Methods Geolocation Processor class


Public:
GeolocationProcessor(String demConfig, String instrumentName, List<String> bulbFilenames)
GeolocationProcessor::preStart
GeolocationProcessor::postEnd
GeolocationProcessor::getNext
GeolocationProcessor::hasNext
GeolocationProcessor::completeProcessing
GeolocationProcessor::process


Private:
GeolocationProcessor::updateStaticDate
GeolocationProcessor::processFileDataset
GeolocationProcessor::processDatasetRecord
GeolocationProcessor::completeRows
GeolocationProcessor::generateInstrumentTiepointRow
GeolocationProcessor::geolocateInstrumentTiePointRow
GeolocationProcessor::processDataset
GeolocationProcessor::setPixelInfor
GeolocationProcessor::orthogeolocation
GeolocationProcessor::timeCorrelation
GeolocationProcessor::obtainOrbitIdInfo
GeolocationProcessor::pixelNumbers
GeolocationProcessor::tiePixelTimeCalibration
GeolocationProcessor::findGeodeticInfoIndex


