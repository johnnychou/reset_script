
import cli_factory as cli

cli_init = {
    'path': '/opt/bin/Infortrend/raidcmd_ESDS10.jar',
    'ip': '10.10.10.200',
    'password': '',
    'cli_retry_time': 1
}

# show_map = cli.ShowMap(cli_init)
show_si = cli.ShowSnapshot(cli_init)
show_part = cli.ShowPartition(cli_init)
show_replica = cli.ShowReplica(cli_init)

delete_si = cli.DeleteSnapshot(cli_init)
delete_part = cli.DeletePartition(cli_init)
delete_replica = cli.DeleteReplica(cli_init)
delete_map = cli.DeleteMap(cli_init)

rc, replica_list = show_replica.execute()
rc, part_list = show_part.execute('-l')
rc, si_list = show_si.execute()

print('Parts: %s' % part_list)

for replica in replica_list:
    print('Delete Replica ID: %s' % replica['Pair-ID'])
    rc, out = delete_replica.execute(replica['Pair-ID'], '-y')

for si in si_list:
    print('Delete SI ID: %s' % si['SI-ID'])
    rc, out = delete_si.execute(si['SI-ID'], '-y')

for part in part_list:
    if part['Mapped'].lower() == 'true':
        print('Delete Map for Part ID: %s' % part['ID'])
        rc, out = delete_map.execute('part',  part['ID'], '-y')
    print('Delete Part ID: %s' % part['ID'])
    rc, out = delete_part.execute(part['ID'], '-y')

