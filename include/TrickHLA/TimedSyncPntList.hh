/*!
@file TrickHLA/TimedSyncPntList.hh
@ingroup TrickHLA
@brief This class extends the TrickHLA::SyncPntListBase class and provides an
instantiable implementation for storing and managing HLA synchronization points
for TrickHLA.

@copyright Copyright 2019 United States Government as represented by the
Administrator of the National Aeronautics and Space Administration.
No copyright is claimed in the United States under Title 17, U.S. Code.
All Other Rights Reserved.

\par<b>Responsible Organization</b>
Simulation and Graphics Branch, Mail Code ER7\n
Software, Robotics & Simulation Division\n
NASA, Johnson Space Center\n
2101 NASA Parkway, Houston, TX  77058

@trick_parse{everything}

@python_module{TrickHLA}

@tldh
@trick_link_dependency{../source/TrickHLA/Int64Time.cpp}
@trick_link_dependency{../source/TrickHLA/SyncPntListBase.cpp}
@trick_link_dependency{../source/TrickHLA/TimedSyncPntList.cpp}

@revs_title
@revs_begin
@rev_entry{Dan Dexter, NASA ER7, TrickHLA, March 2019, --, Version 2 origin.}
@rev_entry{Edwin Z. Crues, NASA ER7, TrickHLA, March 2019, --, Version 3 rewrite.}
@revs_end

*/

#ifndef _TRICKHLA_TIMED_SYNC_PNT_LIST_HH_
#define _TRICKHLA_TIMED_SYNC_PNT_LIST_HH_

// System includes.
#include <string>

// Trick include files.

// TrickHLA include files.
#include "TrickHLA/Int64Time.hh"
#include "TrickHLA/StandardsSupport.hh"
#include "TrickHLA/SyncPntListBase.hh"

// HLA include files.
#include RTI1516_HEADER

namespace TrickHLA
{

class TimedSyncPntList : public TrickHLA::SyncPntListBase
{
   // Let the Trick input processor access protected and private data.
   // InputProcessor is really just a marker class (does not really
   // exists - at least yet). This friend statement just tells Trick
   // to go ahead and process the protected and private data as well
   // as the usual public data.
   friend class InputProcessor;
   // IMPORTANT Note: you must have the following line too.
   // Syntax: friend void init_attr<namespace>__<class name>();
   friend void init_attrTrickHLA__TimedSyncPntList();

  public:
   //
   // Public constructors and destructor.
   //
   /*! @brief Default constructor for the TrickHLA TimedSyncPntList class. */
   TimedSyncPntList();

   /*! @brief Pure virtual destructor for the TrickHLA TimedSyncPntList class. */
   virtual ~TimedSyncPntList()
   {
      return;
   }

   /*! @brief Add the given synchronization point label to the list.
    *  @param label Synchronization point label. */
   virtual void add_sync_pnt( std::wstring const &label );

   /*! @brief Add the given synchronization point label and action time to the list.
    *  @param label Synchronization point label.
    *  @param time  Action time. */
   virtual void add_sync_pnt( std::wstring const &label, const Int64Time &time );

   /*! @brief Achieve all the synchronization points in the list.
    *  @return True is any synchronization point in the list was achieved.
    *  @param rti_ambassador Reference to the HLA RTI Ambassador instance. */
   virtual bool achieve_all_sync_pnts( RTI1516_NAMESPACE::RTIambassador &rti_ambassador )
   {
      Int64Time time( 0.0 );
      return ( achieve_all_sync_pnts( rti_ambassador, time ) );
   }

   /*! @brief Acknowledge all the synchronization point less than or equal to
    * the given time.
    *  @return True if acknowledged, false otherwise.
    *  @param rti_ambassador    Reference to RTI Ambassador.
    *  @param checkTime Time to check. */
   virtual bool achieve_all_sync_pnts( RTI1516_NAMESPACE::RTIambassador &rti_ambassador,
                                       const Int64Time &                 checkTime );

   /*! @brief Determine if we have any synchronization point that has a action
    * time less than the given time.
    *  @return True if sync-point is ready to be cleared.
    *  @param checkTime Time to check. */
   virtual bool check_sync_pnts( const Int64Time &checkTime );

   /*! @brief Converts the vector of synchronization points to a
    *  checkpoint-able class.
    *  @param pts Area to populate. */
   virtual void convert_sync_pts( LoggableSyncPnt *pts );

   /*! @brief Dumps synchronization point information to the screen. */
   virtual void print_sync_pnts();

  private:
   // Do not allow the copy constructor or assignment operator.
   /*! @brief Copy constructor for TimedSyncPntList class.
    *  @details This constructor is private to prevent inadvertent copies. */
   TimedSyncPntList( const TimedSyncPntList &rhs );
   /*! @brief Assignment operator for TimedSyncPntList class.
    *  @details This assignment operator is private to prevent inadvertent copies. */
   TimedSyncPntList &operator=( const TimedSyncPntList &rhs );
};

} // namespace TrickHLA

#endif /* _TRICKHLA_TIMED_SYNC_PNT_LIST_HH_ */
