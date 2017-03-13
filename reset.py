
import cli_factory as cli

cli_init = {
    'path': '/opt/bin/Infortrend/raidcmd_ESDS10.jar',
    'ip': '10.10.10.200',
    'password': '',
    'cli_retry_time': 1
}

# show_map = cli.ShowMap(cli_init)
delete_map = cli.DeleteMap(cli_init)
delete_part = cli.DeletePartition(cli_init)
show_si = cli.ShowSnapshot(cli_init)
show_part = cli.ShowPartition(cli_init)
delete_si = cli.DeleteSnapshot(cli_init)
delete_map = cli.DeleteMap(cli_init)

# print(show_map.execute())

# print(len(list(range(0))))

rc, part_list = show_part.execute()
rc, si_list = show_si.execute()

print(part_list)

for entry in part_list:
    part_id = entry['ID']

    if len(entry['Name']) == 32:
        print('Start Delete Part: %s' % part_id)

        for si_entry in si_list:
            if si_entry['Partition-ID'] == entry['ID']:
                print('Delete SI ID: %s' % si_entry['SI-ID'])
                delete_si.execute(si_entry['SI-ID'], '-y')

        delete_map.execute('part', part_id, '-y')

        print('End Delete Part: %s' % part_id)
        rc, out = delete_part.execute(part_id, '-y')

# Test = [1, 2, 3, 4]

# # Test.remove(1)
# if 1 in Test:
#     Test.remove(1)
# print(Test)

# if 1 in Test:
#     Test.remove(1)
# print(Test)
