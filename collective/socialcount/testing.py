from plone.testing import z2

from plone.app.testing import *
import collective.socialcount

FIXTURE = PloneWithPackageLayer(zcml_filename="configure.zcml",
                                zcml_package=collective.socialcount,
                                additional_z2_products=[],
                                gs_profile_id='collective.socialcount:default',
                                name="collective.socialcount:FIXTURE")

INTEGRATION = IntegrationTesting(bases=(FIXTURE,),
                        name="collective.socialcount:Integration")

FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                        name="collective.socialcount:Functional")

