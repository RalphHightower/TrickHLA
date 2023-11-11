/*!
@file SpaceFOM/PhysicalEntityLagCompInteg.cpp
@ingroup SpaceFOM
@brief This class provides the implementation for a TrickHLA SpaceFOM
physical entity latency/lag compensation class that uses integration to
compensate the state.

@copyright Copyright 2023 United States Government as represented by the
Administrator of the National Aeronautics and Space Administration.
No copyright is claimed in the United States under Title 17, U.S. Code.
All Other Rights Reserved.

\par<b>Responsible Organization</b>
Simulation and Graphics Branch, Mail Code ER7\n
Software, Robotics & Simulation Division\n
NASA, Johnson Space Center\n
2101 NASA Parkway, Houston, TX  77058

@tldh
@trick_link_dependency{../../source/TrickHLA/DebugHandler.cpp}
@trick_link_dependency{../../source/TrickHLA/LagCompensationInteg.cpp}
@trick_link_dependency{PhysicalEntityLagCompInteg.cpp}


@revs_title
@revs_begin
@rev_entry{Edwin Z. Crues, NASA ER7, TrickHLA, November 2023, --, Initial version.}
@revs_end

*/

// System include files.
#include <iostream>
#include <sstream>
#include <string>

// Trick include files.

// TrickHLA include files.
#include "TrickHLA/DebugHandler.hh"
#include "TrickHLA/Attribute.hh"

// SpaceFOM include files.
#include "SpaceFOM/PhysicalEntityLagCompInteg.hh"

using namespace std;
using namespace TrickHLA;
using namespace SpaceFOM;

/*!
 * @job_class{initialization}
 */
PhysicalEntityLagCompInteg::PhysicalEntityLagCompInteg( PhysicalEntityBase & entity_ref ) // RETURN: -- None.
   : PhysicalEntityLagCompBase( entity_ref ),
     TrickHLA::LagCompensationInteg()
{
}


/*!
 * @job_class{shutdown}
 */
PhysicalEntityLagCompInteg::~PhysicalEntityLagCompInteg() // RETURN: -- None.
{
}


/*!
 * @job_class{initialization}
 */
void PhysicalEntityLagCompInteg::initialize()
{
   ostringstream errmsg;

   if ( this->integ_dt < this->integ_tol ) {

      errmsg << "SpaceFOM::PhysicalEntityLagCompInteg::initialize():" << __LINE__<< endl
             << " ERROR: Tolerance must be less that the dt!: dt = "
             << this->integ_dt << "; tolerance = " << this->integ_tol << THLA_ENDL;
      // Print message and terminate.
      TrickHLA::DebugHandler::terminate_with_message( errmsg.str() );

   }

   // Call the base class initialize routine.
   PhysicalEntityLagCompBase::initialize();

   // Return to calling routine.
   return;
}
