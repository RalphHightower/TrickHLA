##############################################################################
# PURPOSE:
#    (This is a Python input file for configuring the Space Reference FOM
#     example Root Reference Frame Publisher (RRFP) federate run.)
#
# REFERENCE:
#    (Trick 17 documentation.)
#
# ASSUMPTIONS AND LIMITATIONS:
#    ((Uses the SpaceFOMFederateConfig Python class.)
#     (Uses the SpaceFOMRefFrameObject Python class.))
#
# PROGRAMMERS:
#    (((Edwin Z. Crues) (NASA/ER7) (Jan 2019) (--) (SpaceFOM support and testing.)))
##############################################################################
import sys
sys.path.append('../../../')
# Load the SpaceFOM specific federate configuration object.
from Modified_data.SpaceFOM.SpaceFOMFederateConfig import *
# Load the SpaceFOM specific reference frame configuration object.
from Modified_data.SpaceFOM.SpaceFOMRefFrameObject import *

def print_usage_message( ):

   print(' ')
   print('TrickHLA SpaceFOM Roles Test Simulation Command Line Configuration Options:')
   print('  -h --help             : Print this help message.')
   print('  -f --fed_name [name]  : Name of the Federate, default is PhysicalEntity.')
   print('  -fe --fex_name [name] : Name of the Federation Execution, default is SpaceFOM_Roles_Test.')
   print('  -m --master [name]    : Name of the Master federate, default is Master.')
   print('  --nostop              : Set no stop time on simulation.')
   print('  -p --pacing [name]    : Name of the Pacing federate, default is Pacing.')
   print('  -s --stop [time]      : Time to stop simulation, default is 10.0 seconds.')
   print('  --verbose [on|off]    : on: Show verbose messages (Default), off: disable messages.')
   print(' ')

   trick.exec_terminate_with_return( -1,
                                     sys._getframe(0).f_code.co_filename,
                                     sys._getframe(0).f_lineno,
                                     'Print usage message.')
   return


def parse_command_line( ) :
   
   global print_usage
   global run_duration
   global verbose
   global federate_name
   global federation_name
   global master_name
   global pacing_name
   global rrfp_name
   
   # Get the Trick command line arguments.
   argc = trick.command_line_args_get_argc()
   argv = trick.command_line_args_get_argv()
   
   # Process the command line arguments.
   # argv[0]=S_main*.exe, argv[1]=RUN/input.py file
   index = 2
   while (index < argc) :
      
      if ((str(argv[index]) == '-h') | (str(argv[index]) == '--help')) :
         print_usage = True
      
      elif ((str(argv[index]) == '-f') | (str(argv[index]) == '--fed_name')) :
         index = index + 1
         if (index < argc) :
            federate_name = str(argv[index])
         else :
            print('ERROR: Missing --fed_name [name] argument.')
            print_usage = True
      
      elif ((str(argv[index]) == '-fe') | (str(argv[index]) == '--fex_name')) :
         index = index + 1
         if (index < argc) :
            federation_name = str(argv[index])
         else :
            print('ERROR: Missing --fex_name [name] argument.')
            print_usage = True
      
      elif ((str(argv[index]) == '-m') | (str(argv[index]) == '--master')) :
         index = index + 1
         if (index < argc) :
            master_name = str(argv[index])
         else :
            print('ERROR: Missing --master [name] argument.')
            print_usage = True 
      
      elif ((str(argv[index]) == '-p') | (str(argv[index]) == '--pacing')) :
         index = index + 1
         if (index < argc) :
            pacing_name = str(argv[index])
         else :
            print('ERROR: Missing --pacing [name] argument.')
            print_usage = True
            
      elif (str(argv[index]) == '-nostop') :
         run_duration = None
      
      elif ((str(argv[index]) == '-s') | (str(argv[index]) == '--stop')) :
         index = index + 1
         if (index < argc) :
            run_duration = float(str(argv[index]))
         else :
            print('ERROR: Missing -stop [time] argument.')
            print_usage = True
      
      elif (str(argv[index]) == '--verbose') :
         index = index + 1
         if (index < argc) :
            if (str(argv[index]) == 'on') :
               verbose = True
            elif (str(argv[index]) == 'off') :
               verbose = False
            else :
               print('ERROR: Unknown --verbose argument: ' + str(argv[index]))
               print_usage = True
         else :
            print('ERROR: Missing --verbose [on|off] argument.')
            print_usage = True
         
      elif ((str(argv[index]) == '-d')) :
         # Pass this on to Trick.
         break
         
      else :
         print('ERROR: Unknown command line argument ' + str(argv[index]))
         print_usage = True
         
      index = index + 1
   return

# Default: Don't show usage.
print_usage = False

# Set the default run duration.
run_duration = 10.0

# Default is to show verbose messages.
verbose = True

# Set the default Federate name.
federate_name = 'RRFP'

# Set the default Federation Execution name.
federation_name = 'SpaceFOM_Roles_Test'

# Set the default Master Federate name.
master_name = 'Master'

# Set the default Paceing Federate name.
pacing_name = 'Pacing'


parse_command_line()

if (print_usage == True) :
   print_usage_message()


#---------------------------------------------
# Set up Trick executive parameters.
#---------------------------------------------
#instruments.echo_jobs.echo_jobs_on()
trick.exec_set_trap_sigfpe(True)
#trick.checkpoint_pre_init(1)
trick.checkpoint_post_init(1)
#trick.add_read(0.0 , '''trick.checkpoint('chkpnt_point')''')

trick.exec_set_enable_freeze(False)
trick.exec_set_freeze_command(False)
trick.sim_control_panel_set_enabled(False)
trick.exec_set_stack_trace(False)


# =========================================================================
# Set up the HLA interfaces.
# =========================================================================
# Instantiate the Python SpaceFOM configuration object.
federate = SpaceFOMFederateConfig( THLA.federate,
                                   THLA.manager,
                                   THLA.execution_control,
                                   THLA.ExCO,
                                   federation_name,
                                   federate_name,
                                   True )

# Set the name of the ExCO S_define instance.
# We do not need to do this since we're using the ExCO default_data job
# to configure the ExCO. This is only needed for input file configuration.
#federate.set_ExCO_S_define_name( 'THLA_INIT.ExCO' )

# Set the debug output level.
if (verbose == True) : 
   federate.set_debug_level( trick.TrickHLA.DEBUG_LEVEL_4_TRACE )
else :
   federate.set_debug_level( trick.TrickHLA.DEBUG_LEVEL_0_TRACE )

#--------------------------------------------------------------------------
# Configure this federate SpaceFOM roles for this federate.
#--------------------------------------------------------------------------
federate.set_master_role( False ) # This is NOT the Master federate.
federate.set_pacing_role( False ) # This is NOT the Pacing federate.
federate.set_RRFP_role( True )    # This is the Root Reference Frame Publisher.

#--------------------------------------------------------------------------
# Add in known required federates.
#--------------------------------------------------------------------------
# This is the RRFP federate.
# It doesn't really need to know about any other federates.
#federate.add_known_fededrate( True, str(federate.federate.name) )
#federate.add_known_fededrate( True, master_name )
#federate.add_known_fededrate( True, pacing_name )

#--------------------------------------------------------------------------
# Configure the CRC.
#--------------------------------------------------------------------------
# Pitch specific local settings designator:
THLA.federate.local_settings = 'crcHost = localhost\n crcPort = 8989'
#THLA.federate.local_settings = 'crcHost = 10.8.0.161\n crcPort = 8989'
# Mak specific local settings designator, which is anything from the rid.mtl file:
#THLA.federate.local_settings = '(setqb RTI_tcpForwarderAddr \'192.168.15.3\') (setqb RTI_distributedForwarderPort 5000)'

#--------------------------------------------------------------------------
# Set up federate related time related parameters.
#--------------------------------------------------------------------------
# Specify the HLA base time units (default: trick.HLA_BASE_TIME_MICROSECONDS).
federate.set_HLA_base_time_units( trick.HLA_BASE_TIME_MICROSECONDS )

# Scale the Trick Time Tic value based on the HLA base time units.
federate.scale_trick_tics_to_base_time_units()

# Must specify a federate HLA lookahead value in seconds.
federate.set_lookahead_time( 0.250 )

# Setup Time Management parameters.
federate.set_time_regulating( True )
federate.set_time_constrained( True )

#--------------------------------------------------------------------------
# Set up CTE time line.
#--------------------------------------------------------------------------
# By setting this we are specifying the use of Common Timing Equipment (CTE)
# for controlling the Mode Transitions for all federates using CTE.
# Don't really need CTE for RRFP.
#THLA.execution_control.cte_timeline = trick.sim_services.alloc_type( 1, 'TrickHLA::CTETimelineBase' )


#---------------------------------------------------------------------------
# Set up for Root Reference Frame data.
#---------------------------------------------------------------------------
root_frame_name = 'RootFrame'
parent_frame_name = ''

root_ref_frame.frame_data.name = root_frame_name
root_ref_frame.frame_data.parent_name = parent_frame_name
                                        
root_ref_frame.frame_data.state.pos[0] = 0.0
root_ref_frame.frame_data.state.pos[1] = 0.0
root_ref_frame.frame_data.state.pos[2] = 0.0
root_ref_frame.frame_data.state.vel[0] = 0.0
root_ref_frame.frame_data.state.vel[1] = 0.0
root_ref_frame.frame_data.state.vel[2] = 0.0
root_ref_frame.frame_data.state.quat_scalar  = 1.0
root_ref_frame.frame_data.state.quat_vector[0] = 0.0
root_ref_frame.frame_data.state.quat_vector[1] = 0.0
root_ref_frame.frame_data.state.quat_vector[2] = 0.0
root_ref_frame.frame_data.state.ang_vel[0] = 0.0
root_ref_frame.frame_data.state.ang_vel[1] = 0.0
root_ref_frame.frame_data.state.ang_vel[2] = 0.0
root_ref_frame.frame_data.state.time = 0.0


ref_frame_A.frame_data.name = 'FrameA'
ref_frame_A.frame_data.parent_name = root_frame_name
                                        
ref_frame_A.frame_data.state.pos[0] = 10.0
ref_frame_A.frame_data.state.pos[1] = 10.0
ref_frame_A.frame_data.state.pos[2] = 10.0
ref_frame_A.frame_data.state.vel[0] = 0.0
ref_frame_A.frame_data.state.vel[1] = 0.0
ref_frame_A.frame_data.state.vel[2] = 0.0
ref_frame_A.frame_data.state.quat_scalar  = 1.0
ref_frame_A.frame_data.state.quat_vector[0] = 0.0
ref_frame_A.frame_data.state.quat_vector[1] = 0.0
ref_frame_A.frame_data.state.quat_vector[2] = 0.0
ref_frame_A.frame_data.state.ang_vel[0] = 0.0
ref_frame_A.frame_data.state.ang_vel[1] = 0.0
ref_frame_A.frame_data.state.ang_vel[2] = 0.0
ref_frame_A.frame_data.state.time = 0.0


#---------------------------------------------------------------------------
# Set up the Root Reference Frame object for discovery.
# If it is the RRFP, it will publish the frame.
# If it is NOT the RRFP, it will subscribe to the frame.
#---------------------------------------------------------------------------
root_frame = SpaceFOMRefFrameObject( federate.is_RRFP,
                                     'RootFrame',
                                     root_ref_frame.frame_packing,
                                     'root_ref_frame.frame_packing' )

# Set the debug flag for the root reference frame.
root_ref_frame.frame_packing.debug = verbose

# Set the root frame for the federate.
federate.set_root_frame( root_frame )

#---------------------------------------------------------------------------
# Set up the Root Reference Frame object for discovery.
# If it is the RRFP, it will publish the frame.
# If it is NOT the RRFP, it will subscribe to the frame.
#---------------------------------------------------------------------------
frame_A = SpaceFOMRefFrameObject( True,
                                  'FrameA',
                                  ref_frame_A.frame_packing,
                                  'ref_frame_A.frame_packing' )

# Set the debug flag for the root reference frame.
ref_frame_A.frame_packing.debug = verbose

# Add this reference frame to the list of managed object.
federate.add_fed_object( frame_A )

#---------------------------------------------------------------------------
# Add the HLA SimObjects associated with this federate.
# This is really only useful for turning on and off HLA objects.
# This doesn't really apply to these example simulations which are only HLA.
#---------------------------------------------------------------------------
federate.add_sim_object( THLA )
federate.add_sim_object( THLA_INIT )
federate.add_sim_object( root_ref_frame )
federate.add_sim_object( ref_frame_A )


#---------------------------------------------------------------------------
# Make sure that the Python federate configuration object is initialized.
#---------------------------------------------------------------------------
#federate.disable()
federate.initialize()


#---------------------------------------------------------------------------
# Set up simulation termination time.
#---------------------------------------------------------------------------
if run_duration:
   trick.sim_services.exec_set_terminate_time( run_duration )
