/*!
@file TrickHLA/Conditional.cpp
@ingroup TrickHLA
@brief This class provides a user API for the handling of a Conditional
attribute.

@copyright Copyright 2019 United States Government as represented by the
Administrator of the National Aeronautics and Space Administration.
No copyright is claimed in the United States under Title 17, U.S. Code.
All Other Rights Reserved.

\par<b>Responsible Organization</b>
Simulation and Graphics Branch, Mail Code ER7\n
Software, Robotics & Simulation Division\n
NASA, Johnson Space Center\n
2101 NASA Parkway, Houston, TX  77058

@tldh
@trick_link_dependency{Conditional.cpp}
@trick_link_dependency{Attribute.cpp}
@trick_link_dependency{Object.cpp}

@revs_title
@revs_begin
@rev_entry{Tony Varesic, L3, DSES, Oct 2009, --, Initial version.}
@rev_entry{Edwin Z. Crues, NASA ER7, TrickHLA, March 2019, --, Version 3 rewrite.}
@rev_entry{Dan Dexter, NASA ER6, TrickHLA, November 2023, --, Added initialize_callback().}
@revs_end

*/

// TrickHLA include files.
#include "TrickHLA/Conditional.hh"
#include "TrickHLA/Attribute.hh"
#include "TrickHLA/Object.hh"

using namespace std;
using namespace TrickHLA;

/*!
 * @job_class{initialization}
 */
Conditional::Conditional() // RETURN: -- None.
   : object( NULL )
{
   return;
}

/*!
 * @job_class{shutdown}
 */
Conditional::~Conditional() // RETURN: -- None.
{
   return;
}

/*!
 * @brief Initialize the callback object to the supplied Object pointer.
 * @param obj Associated object for this class.
 */
void Conditional::initialize_callback(
   Object *obj )
{
   this->object = obj;
}

/*!
 * @brief Default implementation to always send the attribute.
 * @return Defaults to true.
 * @param attr Pointer to TrickHLA Attribute.
 */
bool Conditional::should_send( // RETURN: -- None.
   Attribute *attr )           // IN: ** Attribute data to send
{
   return true;
}
