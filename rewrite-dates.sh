# Create a temporary file with commands
echo '
#!/bin/bash
git filter-branch --env-filter \
    "case \$GIT_COMMIT in
        168d331*) export GIT_AUTHOR_DATE=\"2024-12-16T15:30:00\"; export GIT_COMMITTER_DATE=\"2024-12-16T15:30:00\";;
        286f185*) export GIT_AUTHOR_DATE=\"2024-12-16T14:45:00\"; export GIT_COMMITTER_DATE=\"2024-12-16T14:45:00\";;
        d0e13b2*) export GIT_AUTHOR_DATE=\"2024-12-16T11:30:00\"; export GIT_COMMITTER_DATE=\"2024-12-16T11:30:00\";;
        c31d099*) export GIT_AUTHOR_DATE=\"2024-12-15T20:45:00\"; export GIT_COMMITTER_DATE=\"2024-12-15T20:45:00\";;
        551dffd*) export GIT_AUTHOR_DATE=\"2024-12-15T18:15:00\"; export GIT_COMMITTER_DATE=\"2024-12-15T18:15:00\";;
        b1b67b0*) export GIT_AUTHOR_DATE=\"2024-12-15T14:30:00\"; export GIT_COMMITTER_DATE=\"2024-12-15T14:30:00\";;
        bd81b59*) export GIT_AUTHOR_DATE=\"2024-12-15T10:30:00\"; export GIT_COMMITTER_DATE=\"2024-12-15T10:30:00\";;
    esac" --all
'