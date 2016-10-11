def create_table(table):
    return "CREATE TABLE `frav_ABC`.`" + table + "` (" \
       "`id` INT AUTO_INCREMENT," \
       "`clase` INT," \
       "`file` VARCHAR(255)," \
       "`locateFace` INT," \
       "`faceConfidence` REAL," \
       "`locateEyes` INT," \
       "`eye0Confidence` REAL," \
       "`eye1Confidence` REAL," \
       "`age` INT," \
       "`backgroundUniformity` REAL," \
       "`chin` REAL," \
       "`crown` REAL," \
       "`deviationFromFrontalPose` REAL," \
       "`deviationFromUniformLighting` REAL," \
       "`ear0` REAL," \
       "`ear1` REAL," \
       "`ethnicityAsian` REAL," \
       "`ethnicityBlack` REAL," \
       "`ethnicityWhite` REAL," \
       "`exposure` REAL," \
       "`eye0X` REAL," \
       "`eye0Y` REAL," \
       "`eye0GazeFrontal` REAL," \
       "`eye0Open` REAL," \
       "`eye0Red` REAL," \
       "`eye0Tinted` REAL," \
       "`eye1X` REAL," \
       "`eye1Y` REAL," \
       "`eye1GazeFrontal` REAL," \
       "`eye1Open` REAL," \
       "`eye1Red` REAL," \
       "`eye1Tinted` REAL," \
       "`eyeDistance` REAL," \
       "`faceCenterX` REAL," \
       "`faceCenterY` REAL," \
       "`glasses` REAL," \
       "`grayScaleDensity` INT," \
       "`height` INT," \
       "`hotSpots` INT," \
       "`isColor` INT," \
       "`isMale` REAL," \
       "`lengthOfHead` REAL," \
       "`mouthClosed` REAL," \
       "`naturalSkinColour` REAL," \
       "`numberOfFaces` INT," \
       "`poseAngleRoll` REAL," \
       "`sharpness` REAL," \
       "`width` INT," \
       "`widthOfHead` REAL," \
       "`ISO_19794_5_EyesGazeFrontalBestPractice` INT," \
       "`ISO_19794_5_EyesNotRedBestPractice` INT," \
       "`ISO_19794_5_EyesOpenBestPractice` INT," \
       "`ISO_19794_5_GoodExposure` INT," \
       "`ISO_19794_5_GoodGrayScaleProfile` INT," \
       "`ISO_19794_5_GoodVerticalFacePosition` INT," \
       "`ISO_19794_5_HasNaturalSkinColour` INT," \
       "`ISO_19794_5_HorizontallyCenteredFace` INT," \
       "`ISO_19794_5_ImageWidthToHeightBestPractice` INT," \
       "`ISO_19794_5_IsBackgroundUniformBestPractice` INT," \
       "`ISO_19794_5_IsBestPractice` INT," \
       "`ISO_19794_5_IsCompliant` INT," \
       "`ISO_19794_5_IsFrontal` INT," \
       "`ISO_19794_5_IsFrontalBestPractice` INT," \
       "`ISO_19794_5_IsLightingUniform` INT," \
       "`ISO_19794_5_IsSharp` INT," \
       "`ISO_19794_5_LengthOfHead` INT," \
       "`ISO_19794_5_LengthOfHeadBestPractice` INT," \
       "`ISO_19794_5_MouthClosedBestPractice` INT," \
       "`ISO_19794_5_NoHotSpots` INT," \
       "`ISO_19794_5_NoTintedGlasses` INT," \
       "`ISO_19794_5_OnlyOneFaceVisible` INT," \
       "`ISO_19794_5_Resolution` INT," \
       "`ISO_19794_5_ResolutionBestPractice` INT," \
       "`ISO_19794_5_WidthOfHead` INT," \
       "`ISO_19794_5_WidthOfHeadBestPractice` INT," \
       "`Features_Ethnicity` INT," \
       "`Features_Gender` INT," \
       "`Features_WearsGlasses` INT," \
       "PRIMARY KEY (`id`));"


def generate_query(l, db_name, table):
    var_string = ', '.join(["%s"] * l)
    query_string = "INSERT INTO `" + db_name + "`.`" + table + "` (clase,file,locateFace,faceConfidence,locateEyes,eye0Confidence,eye1Confidence,age,backgroundUniformity,chin,crown,deviationFromFrontalPose,deviationFromUniformLighting,ear0,ear1,ethnicityAsian,ethnicityBlack,ethnicityWhite,exposure,eye0X,eye0Y,eye0GazeFrontal,eye0Open,eye0Red,eye0Tinted,eye1X,eye1Y,eye1GazeFrontal,eye1Open,eye1Red,eye1Tinted,eyeDistance,faceCenterX,faceCenterY,glasses,grayScaleDensity,height,hotSpots,isColor,isMale,lengthOfHead,mouthClosed,naturalSkinColour,numberOfFaces,poseAngleRoll,sharpness,width,widthOfHead,ISO_19794_5_EyesGazeFrontalBestPractice,ISO_19794_5_EyesNotRedBestPractice,ISO_19794_5_EyesOpenBestPractice,ISO_19794_5_GoodExposure,ISO_19794_5_GoodGrayScaleProfile,ISO_19794_5_GoodVerticalFacePosition,ISO_19794_5_HasNaturalSkinColour,ISO_19794_5_HorizontallyCenteredFace,ISO_19794_5_ImageWidthToHeightBestPractice,ISO_19794_5_IsBackgroundUniformBestPractice,ISO_19794_5_IsBestPractice,ISO_19794_5_IsCompliant,ISO_19794_5_IsFrontal,ISO_19794_5_IsFrontalBestPractice,ISO_19794_5_IsLightingUniform,ISO_19794_5_IsSharp,ISO_19794_5_LengthOfHead,ISO_19794_5_LengthOfHeadBestPractice,ISO_19794_5_MouthClosedBestPractice,ISO_19794_5_NoHotSpots,ISO_19794_5_NoTintedGlasses,ISO_19794_5_OnlyOneFaceVisible,ISO_19794_5_Resolution,ISO_19794_5_ResolutionBestPractice,ISO_19794_5_WidthOfHead,ISO_19794_5_WidthOfHeadBestPractice,Features_Ethnicity,Features_Gender,Features_WearsGlasses) VALUES (%s);" % var_string
    return query_string