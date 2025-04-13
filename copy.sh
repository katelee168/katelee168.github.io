cp ../pandoc-markdown-css-theme/src/training-data/katherine.md index.mmd
cp ../pandoc-markdown-css-theme/docs/training-data/katherine.html index.html

# Copy CSS
source_dir="/Users/katherine/Projects/pandoc-markdown-css-theme/docs/training-data/css/"
destination_dir="/Users/katherine/Projects/katelee168.github.io/css/"
file_list=("theme" "theme-additions")

for filename in "${file_list[@]}"
do
    source_path="${source_dir}${filename}.css"
    destination_path="${destination_dir}${filename}.css"

    cp "$source_path" "$destination_path" && echo "Copied: $filename"
done
